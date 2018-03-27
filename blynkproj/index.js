var Blynk = require('blynk-library');
var piblaster = require('pi-blaster.js');

var AUTH = 'ccdebc73fc584feead43a8e381ec1662';

var blynk = new Blynk.Blynk(AUTH, options= {connector: new Blynk.TcpClient( options = { addr:"127.0.0.1", port:8442 } )
});

var avancer = new blynk.VirtualPin(1);
var reculer = new blynk.VirtualPin(2);
var gauche = new blynk.VirtualPin(3);
var droite = new blynk.VirtualPin(4);
var stop = new blynk.VirtualPin(5);

var Gpio = require('onoff').Gpio,
  dirIn1 = new Gpio(17, 'out'),
  dirIn2 = new Gpio(18, 'out'),
  dirPWM = new Gpio(27, 'out'),
  dirD1 = new Gpio(22, 'out'),
  dirEN = new Gpio(23, 'out'),
  motInA = new Gpio(6, 'out'),
  motInB = new Gpio(12, 'out'),
  motPWM = new Gpio(13, 'out');

avancer.on('write', function(param) {
  piblaster.setPwm(23, 1),
  piblaster.setPwm(24, 0),
  piblaster.setPwm(18, param[0]);
});

reculer.on('write', function(param) {
  piblaster.setPwm(23, 0),
  piblaster.setPwm(24, 1),
  piblaster.setPwm(18, param[0]);
});

gauche.on('write', function(param) {
  piblaster.setPwm(17, 0),
  piblaster.setPwm(18, 1),
  piblaster.setPwm(22, 0),
  piblaster.setPwm(27, param[0]),
  piblaster.setPwm(23, 1);
});
