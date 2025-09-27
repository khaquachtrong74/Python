{pkgs ? import<nixpkgs>{}}:
pkgs.mkShell{
    buildInputs = with pkgs;[
        python312
        python312Packages.django
#        pyright
    ];
    packages = with pkgs;[
        # Add Python packages, for global    
        pyright
    ];
}
