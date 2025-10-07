# GTK Exercise Collection

** COPYING template FOLDER FOR BUILD, SHOULD NOT CHANGE IT **

**复制 template 文件夹去构建，不要直接使用和修改模板**！！！

## Template

The [template](template/) fork from [GTK Rust Template](https://gitlab.gnome.org/World/Rust/gtk-rust-template). Changed for support Adwaita theme.

### Usage

1. System: Fedora Sliverblue
2. Container tool: Toolbox
3. IDE: Visual Studio Code
4. VSCode Extemsions:
    - Even Better TOML (@tamasfe)
    - Meson (@mesonbuild)
    - EditorConfig for VS Code (@EditorConfig)
    - Flatpak (@Bilal Elmoussaoui)
    - Gtk Blueprint (@Bodil Stokke)
    - rust-analyzer (@The Rust Programming Language)
5. VSCode Settings:

```js
"search.exclude": {
    "**/_build": true,
    "**/target": true,
    "**/.flatpak": true,
    "**/.gnome-builder": true,
    "**/.cargo": true
},
"files.exclude": {
    "**/.flatpak": true,
    "**/.gnome-builder": true
}
```

6. Flatpak required:
    - org.gnome.Platform
    - org.gnome.Sdk
    - org.freedesktop.Sdk
    - org.freedesktop.Sdk.Extension.rust-stable
    - org.freedesktop.Sdk.Extension.llvm19

7. Development environment required:
    - `flatpak-builder`
    - `default-fonts-cjk`
    - `rust-libadwaita-devel`
    - `blueprint-compiler`

## Sub Projects

1. [Hello Button](hello_button/)

