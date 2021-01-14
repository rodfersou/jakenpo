with import <nixpkgs> {};
mkShell {
  name = "rps-shell";
  shellHook = ''
  '';
  buildInputs = [
    python38
  ];
}
