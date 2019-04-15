'use strict';
var SEP = {};
SEP.Node = {};
SEP.ele ={};
SEP.App ={};
SEP.ai ={};
var LOCAL ={};

SEP.appInit = function () {
    try {
        SEP.initSerial();
        SEP.initOther();
    }
    catch (error) {
        console.error(error);
    }
};

SEP.initSerial = function () {
    try {
        SEP.SerialPort = require('serialport');
        SEP.Avrgirl = require('avrgirl-arduino');
        SEP.avrpizza = require('avr-pizza');
        SEP.write = function (port,hexData,back) {
            try{
                //console.log('发送：' + hexData);
                var buffer = new Buffer(hexData, "hex");
                port.write(buffer, function (err) {
                    if (err) {
                        return console.log('Error: ', err.message)
                    }
                })
                ;
            }catch (error){console.error(error);}
        }
    }
    catch (error) {
        console.error(error);
    }
};

SEP.initOther =function() {
    SEP.Node.fs = require('fs');
    SEP.Node.http = require('http');
    SEP.Node.os = require('os');
    const {shell, remote, ipcRenderer} = require('electron');
    const isDev = require('electron-is-dev');
    SEP.ele.isDev = isDev;
    SEP.ele.shell =shell;
    SEP.ele.remote = remote;
    SEP.ele.ipcRenderer = ipcRenderer;
    SEP.Node.request = require('request');
    SEP.Node.baiduAi = require("../node/baidu-ai").speech;
    let dir = '';
    if (__dirname.indexOf('app.asar') !== -1) {
        const reg = /app.asar.+$/g;
        dir = __dirname.replace(reg, '');
    } else {
        dir = `${__dirname}/../`;
    }
    SEP.ele.dir = `${dir}`;
};

SEP.appInit();

//myserial

//gsApp
