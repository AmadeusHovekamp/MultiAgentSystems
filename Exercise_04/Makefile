# Zu verwendende Shell umstellen, damit Brace Extensions funktionieren.
SHELL=/bin/bash

TEX_FILES=$(wildcard *.tex)
<<<<<<< HEAD
TARGET=Exercise_04
=======
TARGET=Exercise_03
>>>>>>> 5868a11d1b2d9b44ada4513efeec7d32bc50073a

$(TARGET).pdf: $(TEX_FILES)
	xelatex $(TARGET)
	xelatex $(TARGET)

clean:
	$(RM) *.{aux,log,out}
.PHONY: clean

distclean:
	$(RM) $(TARGET).pdf *.{aux,log,out}
.PHONY: distclean
