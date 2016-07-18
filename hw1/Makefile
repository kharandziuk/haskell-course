test: compile rm_temp
	./main
rm_temp:
	rm *.hi *.o
compile: main.hs
	ghc -o main main.hs
