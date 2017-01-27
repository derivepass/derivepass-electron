package: build clean
	./node_modules/.bin/electron-packager --icon=icons/mac.icns . DerivePass

clean:
	rm -rf ./DerivePass-*/

build:
	PATH="${PWD}/.bin:${PATH}" HOME=~/.electron-gyp \
		node-gyp configure --target=1.4.13 \
		--dist-url=https://atom.io/download/electron
	node-gyp build

build-test:
	PATH="${PWD}/.bin:${PATH}" node-gyp configure
	node-gyp build

.PHONY: package build build-test clean
