const express = require('express');
const bodyParser = require('body-parser');
const app = express();

app.use(bodyParser.urlencoded({extended: false}));

/* global SEP:true */

app.get('/', (req, res) => {
    res.send('Hello Robobloq!');
});
// 设置电机前后左右运动,速度默认为80
app.post('/set_motor_type', (req, res) => {
    const data = req.body;
    SEP.RobotBlocks.gs_motion_move_2(data);
    res.send('success');
});

// 设置板载电机“M1/M2”“顺时针/逆时针”运动，以速度“输入框”
app.post('/set_motor_direction', (req, res) => {
    const data = req.body;
    SEP.RobotBlocks.gs_motion_motor_direction(data);
    res.send('success');
});

app.post('/set_motor_stop', (req, res) => {
    const data = req.body;
    SEP.RobotBlocks.gs_motion_stopMove(data);
    res.send('success');
});

app.post('/set_external_motor', (req, res) => {
    const data = req.body;
    SEP.RobotBlocks.gs_motion_external_motor(data);
    res.send('success');
});

app.post('/motion_steering_engine', (req, res) => {
    const data = req.body;
    SEP.RobotBlocks.gs_motion_external_motor(data);
    res.send('success');
});

app.post('/show_matrix', (req, res) => {
    const data = req.body;
    SEP.RobotBlocks.gs_matrix_change_9(data);
    res.send('success');
});

app.post('/hide_matrix', (req, res) => {
    const data = req.body;
    SEP.RobotBlocks.gs_matrix_change_9(data);
    res.send('success');
});

app.post('/set_led', (req, res) => {
    const data = req.body;
    SEP.RobotBlocks.gs_light_change_2(data);
    res.send('success');
});

app.post('/set_ultrasonic', (req, res) => {
    const data = req.body;
    SEP.RobotBlocks.gs_light_ultrasonic_2(data);
    res.send('success');
});

app.post('/set_sound', (req, res) => {
    const data = req.body;
    SEP.RobotBlocks.gs_sound_play(data);
    res.send('success');
});
/**
 * 获取超声波传感器的值-
 */
app.post('/get_ultrasonic', async (req, res) => {
    const data = req.body;
    const result = await SEP.RobotBlocks.gs_sensing_distanceto(data);
    res.json(parseFloat(result));
});
/**
 * 获取巡线传感器的值-
 */
app.post('/get_line_patrol', async (req, res) => {
    const data = req.body;
    const result = await SEP.RobotBlocks.gs_sensing_linePatrolValue(data);
    res.json(parseFloat(result));
});

/**
 * 获取巡线传感器的值-
 */
app.post('/get_line_patrol2', async (req, res) => {
    const data = req.body;
    const result = await SEP.RobotBlocks.gs_sensing_linePatrolValue2(data);
    res.json(parseFloat(result));
});
/**
 * 获取声音传感器的值-
 */
app.post('/get_sound', async (req, res) => {
    const data = req.body;
    const result = await SEP.RobotBlocks.gs_sensing_voiceValue(data);
    res.json(parseFloat(result));
});
/**
 * 获取光线传感器的值-
 */
app.post('/get_light', async (req, res) => {
    const data = req.body;
    const result = await SEP.RobotBlocks.gs_sensing_lightValue(data);
    res.json(parseFloat(result));
});
/**
 * 获取温度传感器的值-
 */
app.post('/get_temperature', async (req, res)=>{
    const data = req.body;
    const result = await SEP.RobotBlocks.gs_sensing_temperatureValue(data);
    res.json(parseFloat(result));
});
/**
 * 获取湿度传感器的值-
 */
app.post('/get_humidity', async (req, res)=>{
    const data = req.body;
    const result = await SEP.RobotBlocks.gs_sensing_humidityValue(data);
    res.json(parseFloat(result));
});
/**
 * 获取人体红外传感器-
 */
app.post('/get_infraredValue', async (req, res)=>{
    const data = req.body;
    const result = await SEP.RobotBlocks.gs_sensing_infraredValue(data);
    res.json(parseFloat(result));
});
/**
 * 获取陀螺仪传感器的值-
 */
app.post('/getSensingGyroValue', async (req, res)=>{
    const data = req.body;
    const result = await SEP.RobotBlocks.gs_sensing_gyroValue(data);
    res.json(parseFloat(result));
});

/**
 * 获取颜色传感器的值-
 */
app.post('/gsSensingColor', async (req, res)=>{
    const data = req.body;
    const result = await SEP.RobotBlocks.gsSensingColor(data);
    res.json(parseFloat(result));
});
/**
 * 获取颜色传感器灰度值-
 */
app.post('/gsSensingColorGrey', async (req, res)=>{
    const data = req.body;
    const result = await SEP.RobotBlocks.gsSensingColorGrey(data);
    res.json(parseFloat(result));
});

app.post('/gs_matrix_rgb_led4', async (req, res)=>{
    const data = req.body;
    const result = await SEP.RobotBlocks.gs_matrix_rgb_led4(data);
    res.json(parseFloat(result));
});

app.post('/gs_sensing_mp3Play2', async (req, res)=>{
    const data = req.body;
    const result = await SEP.RobotBlocks.gs_sensing_mp3Play2(data);
    res.json(parseFloat(result));
});

app.post('/gs_sensing_mp3Play3', async (req, res)=>{
    const data = req.body;
    const result = await SEP.RobotBlocks.gs_sensing_mp3Play3(data);
    res.json(parseFloat(result));
});

app.post('/shows_digital1', async (req, res) => {
    const data = req.body;
    const result = await SEP.RobotBlocks.gs_shows_digital1(data);
    res.json(parseFloat(result));
});

app.post('/shows_digital2', async (req, res) => {
    const data = req.body;
    const result = await SEP.RobotBlocks.gs_shows_digital2(data);
    res.json(parseFloat(result));
});

app.post('/shows_digital3', async (req, res) => {
    const data = req.body;
    const result = await SEP.RobotBlocks.gs_shows_digital3(data);
    res.json(parseFloat(result));
});

app.post('/shows_digital4', async (req, res) => {
  const data = req.body;
  const result = await SEP.RobotBlocks.gs_shows_digital4(data);
  res.json(parseFloat(result));
});

app.post('/set_led_animal', async (req, res) => {
    const data = req.body;
    const result = await SEP.RobotBlocks.gs_looks_setledanimal(data);
    res.json(parseFloat(result));
});

app.post('/set_led_color', async (req, res) => {
    const data = req.body;
    const result = await SEP.RobotBlocks.gs_looks_setledcolor(data);
    res.json(parseFloat(result));
});

app.post('/close_led', async (req, res) => {
    const data = req.body;
    const result = await SEP.RobotBlocks.gs_looks_close_led(data);
    res.json(parseFloat(result));
});

app.post('/get_temperature2', async (req, res) => {
    const data = req.body;
    const result = await SEP.RobotBlocks.gs_sensing_temperatureValue2(data);
    res.json(parseFloat(result));
});

app.listen(12345, '127.0.0.1', () => console.log('Example app listening on port 12345!'));
