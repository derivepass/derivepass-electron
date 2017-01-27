{
  "variables": {
    "gypkg_deps": [
      "git://github.com/indutny/scrypt.git@^1.0.1 [gpg] => scrypt.gyp:scrypt",
      "git://github.com/indutny/derivepass.git@^1.0.0 [gpg] => derivepass.gyp:derivepass",
    ],
  },

  "targets": [{
    "target_name": "scrypt_binding",
    # Uncomment to generate freeze file
    # "type": "<!(gypkg type)",
    "dependencies": [
      "<!@(gypkg deps <(gypkg_deps))"
    ],
    "include_dirs": [
      ".",
      "<!(node -e \"require('nan')\")",
    ],
    "sources": [
      "src/scrypt.cc"
    ],
  }],
}
