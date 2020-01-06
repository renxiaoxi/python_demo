const gulp = require('gulp');
const imagemin = require('gulp-imagemin')
const uglify = require('gulp-uglify')
const sass = require('gulp-sass')
const concat = require('gulp-concat')
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




// copy all HTML files
gulp.task('copyHtml', function () {
   gulp.src('src/*.html')
      .pipe(gulp.dest('dist'));
})

// gulp.task('minify', function () {
//    gulp.src('src/js/*.js')
//       .pipe(uglify())
//       .pipe(gulp.dest('dist/js'));
// })

// optimize Images
gulp.task('imagemin', function () {
   gulp.src('src/images/*')
      .pipe(imagemin())
      .pipe(gulp.dest('dist/images'))
})

// compile sass
gulp.task('sass', function(){
   gulp.src('src/sass/*.scss')
      .pipe(sass().on('error', sass.logError))
      .pipe(gulp.dest('dist/css'))
});

// js
gulp.task('scripts', function(){
   gulp.src('src/js/*.js')
      .pipe(concat('main.js'))
      .pipe(uglify())
      .pipe(gulp.dest('dist/js'))
})



gulp.task('default',gulp.parallel('message','copyHtml','sass','imagemin','scripts'));

gulp.task('watch', function(){
   gulp.watch('src/js/*.js',gulp.parallel('scripts'));
   gulp.watch('src/css/*.scss',gulp.parallel('sass'));
   gulp.watch('src/image/*',gulp.parallel('imagemin'));
   gulp.watch('src/*.html',gulp.parallel('copyHtml'));
})