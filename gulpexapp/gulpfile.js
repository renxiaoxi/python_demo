const gulp = require('gulp');
const imagemin = require('gulp-imagemin')


/*

TOP LEVEL FUNCTIONS

gulp.task - define tasks
gulp.src - point files to use
gulp.dest - point to folder to output
gulp.watch - watch file for changes


 */


// log message
gulp.task('message', function () {
   return console.log('gulp is running ...');
})

gulp.task('default', function () {
   return console.log('gulp is running ...');
})


// copy all HTML files
gulp.task('copyHtml', function () {
   gulp.src('src/*.html')
      .pipe(gulp.dest('dist'));
})

// optimize Images
gulp.task('imagemin', function () {
   gulp.src('src/images/*')
      .pipe(imagemin())
      .pipe(gulp.dest('dist/images'))
})