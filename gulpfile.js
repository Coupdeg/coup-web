'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass');

gulp.task('scss', function () {
	setInterval(function() {			
		gulp.src('./coupdeg/static/scss/app.scss')
		.pipe(sass())
		.pipe(gulp.dest('./coupdeg/static/css'));
	}, 5000)	
});
gulp.task('default', ['scss']);