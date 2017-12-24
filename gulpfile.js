var browserSync = require('browser-sync');
var gulp = require('gulp');
var sass = require('gulp-sass');
var cleanCSS = require('gulp-clean-css');
var uglify = require('gulp-uglify');






// Partie Browser-sync
gulp.task('browser-sync', function() {
    browserSync.init({
        server: {
            baseDir: "./"
        }
    });
    
});

// Partie Sass 
gulp.task('sass', function () {
  return gulp.src('./assets/scss/*.scss')
    .pipe(sass())
    .pipe(cleanCSS())
    .pipe(gulp.dest('./dist/css'))
    // .pipe(browserSync.stream())
});



// Partie gulp-uglify
gulp.task('uglify', function () {

    gulp.src('assets/js/*.js')
    .pipe(uglify())
    .pipe(gulp.dest('dist/js/'))
    // .pipe(browserSync.stream())
});


// Partie Gulp general 
gulp.task('default',['browser-sync','sass','uglify'], function() {
    gulp.watch('assets/scss/*.scss', ['sass']).on('change', browserSync.reload);
    gulp.watch('assets/js/*.js', ['uglify']).on('change', browserSync.reload);
    gulp.watch("*.html").on('change', browserSync.reload);
    
});