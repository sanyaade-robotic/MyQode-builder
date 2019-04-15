var net = require('net');

var server = net.createServer((socket) => {
    // socket.write('Echo server\r\n');
    // socket.pipe(socket);
    socket.on('data', (bytes) => {
        /* global SEP:true */
        const str = bytes.toString();
        const result = JSON.parse(str);
        switch (result.event) {
        case 'set_motor':
            SEP.RobotBlocks.gs_motion_move_3(result.data);
            break;
        case 'show_matrix':
            SEP.RobotBlocks.gs_matrix_change_9(result.data);
            break;
        case 'hide_matrix':
            SEP.RobotBlocks.gs_matrix_change_9(result.data);
            break;
        case 'set_led':
            SEP.RobotBlocks.gs_light_change_2(result.data);
            break;
        case 'set_ultrasonic':
            SEP.RobotBlocks.gs_light_ultrasonic_2(result.data);
            break;
        case 'set_sound':
            SEP.RobotBlocks.gs_sound_play(result.data);
            break;
        case 'get_ultrasonic':
            SEP.RobotBlocks.gs_sound_play(result.data);
            break;
        case 'get_line_patrol':
            SEP.RobotBlocks.gs_sound_play(result.data);
            break;
        case 'get_sound':
            SEP.RobotBlocks.gs_sound_play(result.data);
            break;
        case 'get_light':
            SEP.RobotBlocks.gs_sound_play(result.data);
            break;
        default:
            console.error('Unexpected event.');
        }

    });
});

server.listen(12345, '127.0.0.1');
