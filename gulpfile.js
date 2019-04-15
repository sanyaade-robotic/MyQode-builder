const gulp = require('gulp');
const electron = require('electron-connect').server.create();

gulp.task('default', function () {
  electron.start();
  gulp.watch(['./www/build/*.js'], electron.restart);
  gulp.watch(['./www/build/*.{html,js,css}'], electron.reload);
});
