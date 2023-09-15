help:
	@echo 'Makefile for a hugo Web site                                           '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make html                           (re)generate the web site          '
	@echo '   make clean                          remove the generated files         '
	@echo '   make serve                          serve site at http://localhost:1313'
	@echo '   make github                         upload the web site via gh-pages   '
	@echo '                                                                          '

html:
	hugo

clean:
	[ ! -d public ] || rm -rf public

serve:
	hugo server

# Doesn't work!
github: html
	cd public 
	git commit -a -m "Generate Hugo site"
	git push
