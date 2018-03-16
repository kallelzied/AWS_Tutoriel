'use strict';

module.exports.sendReminderAlarm = (event, context, callback) => {
    
    var AWS = require('aws-sdk');
    AWS.config.update({region:'eu-west-1'});
    var ses = new AWS.SES();
    var fs = require('fs');

    var fromAdress = 'kallelzied@live.com'
    var toAdress = 'kallelzied@gmail.com'
    var params = {
        Destination: {
            ToAddresses: [toAdress]
        },
        Message: {
            Body: {
                Text: {
                    Charset: "UTF-8", 
                    Data: "It is a now day Get up and make the world perfect"
                }, 
                Text: {
                    Charset: "UTF-8", 
                    Data: "Remember to continue helping the universe!"
                }
            }, 
            Subject: {
                Charset: "UTF-8", 
                Data: "Daily Reminder Alarm"
            }
        },
        ReplyToAddresses: [fromAdress],
        Source: fromAdress, 
    };

    ses.sendEmail(params, function(err, data) {
        // an error occurred
        if (err) console.log(err, err.stack); 
        // successful response
        else callback(null, data);
    }); 
};