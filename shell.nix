{ pkgs ? import <nixpkgs> {}}:


pkgs.mkShell {
    buildInputs = [
        (pkgs.python3.withPackages (python-pkgs: [
            python-pkgs.pandas
            python-pkgs.pyarrow
            python-pkgs.duckdb
            python-pkgs.matplotlib
            python-pkgss.seaborn
            python-pkgs.ipykernel
        ]))
    ];
}