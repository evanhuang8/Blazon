module.exports = (grunt) ->

    grunt.loadNpmTasks 'grunt-bower-concat'
    grunt.loadNpmTasks 'grunt-concurrent'
    grunt.loadNpmTasks 'grunt-contrib-coffee'
    grunt.loadNpmTasks 'grunt-contrib-uglify'
    grunt.loadNpmTasks 'grunt-contrib-jade'
    grunt.loadNpmTasks 'grunt-contrib-less'
    grunt.loadNpmTasks 'grunt-contrib-concat'
    grunt.loadNpmTasks 'grunt-env'
    grunt.loadNpmTasks 'grunt-newer'
    grunt.loadNpmTasks 'grunt-prompt'
    grunt.loadNpmTasks 'grunt-shell'
    grunt.loadNpmTasks 'grunt-simple-watch'

    grunt.initConfig
        env:
            dev:
                MASTERCARD_PUBLIC: 'sbpb_NjIxZjhlYTktNTQxMS00NzI1LWFhMGQtOGY1YjJiMDZlMGFh'
                MASTERCARD_PRIVATE: '/6XxzS5TE28m7PD4E2Ykk4ImRgqstQzJhwfQ+/sxtOp5YFFQL0ODSXAOkNtXTToq'
        bower_concat:
            libraries:
                dest: 'sponsorship/static/js/libraries.js'
                mainFiles: 
                    'foundation': [
                        'js/foundation.js'
                        'js/foundation/foundation.abide.js'
                    ]
        coffee:
            compile:
                files: [
                    expand: true
                    cwd: 'views/js/'
                    src: ['**/*.coffee']
                    dest: 'sponsorship/static/js/'
                    ext: '.js'
                ]
        jade:
            compile: 
                options:
                    data:
                        debug: false
                        pretty: false
                files: [
                    expand: true
                    cwd: 'views/templates/'
                    src: ['**/*.jade']
                    dest: 'sponsorship/templates/'
                    ext: '.html'
                ]
        less:
            compile:
                options:
                    compress: true
                files:
                    'sponsorship/static/css/blazon.css': 'views/css/blazon.less'
        watch:
            jade:
                options:
                    nospawn: true
                files: ['views/templates/**/*.jade']
                tasks: ['jade']
            coffee:
                options:
                    nospawn: true
                files: ['views/js/**/*.coffee']
                tasks: ['newer:coffee']
            less:
                options:
                    nospawn: true
                files: ['views/css/**/*.less']
                tasks: ['less']
        shell:
            server:
                options:
                    stdout: true
                    stderr: true
                command: 'python manage.py runserver 0.0.0.0:8080'
            test:
                options:
                    stdout: true
                    stderr: true
                command: 'python manage.py test sponsorship.tests'
        concurrent:
            startDevelopment:
                tasks: [
                    'simple-watch'
                    'shell:server'
                ]
                options:
                    limit: 10
                    logConcurrentOutput: true

    grunt.option('force', true)

    grunt.registerTask 'compile', ['jade', 'coffee', 'less', 'bower_concat']
    
    grunt.registerTask 'dev', ['compile', 'env:dev', 'concurrent:startDevelopment']

    grunt.registerTask 'test', ['shell:test']

    return