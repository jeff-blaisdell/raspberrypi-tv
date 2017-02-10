// [START app]
'use strict';

process.env.DEBUG = 'actions-on-google:*';

let ActionsSdkAssistant = require('actions-on-google').ActionsSdkAssistant;
let express = require('express');
let bodyParser = require('body-parser');
let unirest = require('unirest');
let secrets = require('./secrets');
let noInputs = [
  'Could you speak up? <break time="1s" /> My ears are not what they once were.',
  'I love the sound of your voice. <break time="1s" /> I just wish I could hear it!',
  'I beg your pardon, <break time="1s" /> but could you please speak up?'
];

let app = express();
app.set('port', (process.env.PORT || 8080));
app.use(bodyParser.json({type: 'application/json'}));

app.post('/', function (request, response) {
  console.log('handle post');
  let assistant = new ActionsSdkAssistant({request: request, response: response});

  function mainIntent (assistant) {
    console.log('mainIntent');
    assistant.ask(
            assistant.buildInputPrompt(true, '<speak>Hi! <break time="1"/> How may I serve you?', noInputs)
        );
  }

  function rawInput (assistant) {
    console.log('rawInput');
    if (assistant.getRawInput() in ['bye', 'close', 'no']) {
      assistant.tell('Goodbye!');
      return;
    }

    unirest.post(`${secrets.host}/execute`)
            .headers({'Accept': 'application/json', 'Content-Type': 'application/json'})
            .auth({ user: secrets.auth.user, pass: secrets.auth.pass })
            .send({ text: assistant.getRawInput() })
            .end(function (response) {
              if (response.notFound) {
                assistant.ask(
                      assistant.buildInputPrompt(
                          false,
                          'Pardon, but I could not find a device with that command.  ' +
                          'May I help you with anything else?',
                          noInputs
                      )
                  );
              } else if (!response.ok) {
                assistant.ask(
                      assistant.buildInputPrompt(
                          false,
                          'I\'m very embarrassed, but I was not able to help with your request.' +
                          'May I help you with anything else?',
                          noInputs
                      )
                  );
              } else {
                assistant.ask(
                      assistant.buildInputPrompt(
                          false,
                          'May I help you with anything else?',
                          noInputs
                      )
                  );
              }
            });
  }

  let actionMap = new Map();
  actionMap.set(assistant.StandardIntents.MAIN, mainIntent);
  actionMap.set(assistant.StandardIntents.TEXT, rawInput);

  assistant.handleRequest(actionMap);
});

// Start the server
let server = app.listen(app.get('port'), function () {
  console.log('App listening on port %s', server.address().port);
  console.log('Press Ctrl+C to quit.');
});
// [END app]
