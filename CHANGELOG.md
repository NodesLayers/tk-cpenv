# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [v0.3.2](https://github.com/cpenv/tk-cpenv/releases/tag/v0.3.2) ([compare](https://github.com/cpenv/tk-cpenv/compare/v0.3.1...v0.3.2)) - 2020-08-05

### Added
- Add: preview environment tool ([8baf4ce](https://github.com/cpenv/tk-cpenv/commit/8baf4ce870a102fca51fa8a6ffab89045a054bf4) by Dan Bradham).

### Changed
- Change: update readme.md - add "use set modules dialog" section ([920fdad](https://github.com/cpenv/tk-cpenv/commit/920fdadc23e208ec14806b0798a14da52f0146f7) by Dan Bradham).
- Change: maintain user ordering of selected modules list ([5fa4a08](https://github.com/cpenv/tk-cpenv/commit/5fa4a08b6534342c2a3cee94d46bc7efa965ff67) by Dan Bradham).
- Change: update cpenv to 0.5.8 ([d1e11ad](https://github.com/cpenv/tk-cpenv/commit/d1e11ad75f3bc53b5bf82d727acd74228cd8eeb1) by Dan Bradham).
- Change: update readme.md ([091a497](https://github.com/cpenv/tk-cpenv/commit/091a497d8096936985ed0024d502e516756cfa12) by Dan Bradham).

### Fixed
- Fix: patch cpenv imports ([7ea6554](https://github.com/cpenv/tk-cpenv/commit/7ea655442285858ef2d3ab5bae1dee49354f84d8) by Dan Bradham).

### Misc
- Update readme.md ([449bf78](https://github.com/cpenv/tk-cpenv/commit/449bf78626dde9c58be4b483cc8fa059c9289ca4) by Dan Bradham).


## [v0.3.1](https://github.com/cpenv/tk-cpenv/releases/tag/v0.3.1) ([compare](https://github.com/cpenv/tk-cpenv/compare/v0.2.2...v0.3.1)) - 2020-06-30

### Added
- Add: store environments directly in the shotgun database. closes #3 add: create environments per project / engine add: import environments from other projects fix: fix progress reporting. closes #2 ([dcf0658](https://github.com/cpenv/tk-cpenv/commit/dcf0658899ed17fc731e99ec986439637990d99d) by Dan Bradham).

### Changed
- Change: update cpenv to 0.5.7 ([9fdeb7f](https://github.com/cpenv/tk-cpenv/commit/9fdeb7f97e4bc17e040ed3ce5081574396ec6979) by Dan Bradham).
- Change: bump version in example_config ([55924f4](https://github.com/cpenv/tk-cpenv/commit/55924f49583885c04985e8c521809a8bd6ff0b1d) by Dan Bradham).

### Fixed
- Fix: include shotgun_api3.lib package ([341c32d](https://github.com/cpenv/tk-cpenv/commit/341c32d084daa434d62ef0cb415d3719e38fd744) by Dan Bradham).
- Fix: attributeerror in before_app_launch ([e35eedc](https://github.com/cpenv/tk-cpenv/commit/e35eedc1978e3caf0aaaa4fb7bbf492bfdcdfeb1) by Dan Bradham).

### Misc
- Update readme.md ([2cfbd7a](https://github.com/cpenv/tk-cpenv/commit/2cfbd7a92493945426ff7d5541cc9e46e1c4dde2) by Dan Bradham).


## [v0.2.2](https://github.com/cpenv/tk-cpenv/releases/tag/v0.2.2) ([compare](https://github.com/cpenv/tk-cpenv/compare/v0.2.1...v0.2.2)) - 2020-05-26

### Changed
- Change: update cpenv to 0.5.4 ([3c93ea5](https://github.com/cpenv/tk-cpenv/commit/3c93ea5186a79fed46186f729152697146f95b0d) by Dan Bradham).

### Misc
- Update readme.md ([fd325f4](https://github.com/cpenv/tk-cpenv/commit/fd325f4cbfaa655f16e10017bc64afe0ab9b8db9) by Dan Bradham).


## [v0.2.1](https://github.com/cpenv/tk-cpenv/releases/tag/v0.2.1) ([compare](https://github.com/cpenv/tk-cpenv/compare/v0.2.0...v0.2.1)) - 2020-05-18

### Added
- Add: uireporter, progressdialog and errordialog ([c21f616](https://github.com/cpenv/tk-cpenv/commit/c21f6160c7de75f08d0d50a5f5cef72af9285eec) by Dan Bradham).

### Changed
- Change: bump version in example_config ([aacc658](https://github.com/cpenv/tk-cpenv/commit/aacc65817e87e73b47dc1688a635398ab073e733) by Dan Bradham).
- Change: update readme ([88e1427](https://github.com/cpenv/tk-cpenv/commit/88e142731c6fae9ec24095418673f865761717ec) by Dan Bradham).
- Change: update cpenv to 0.5.2 ([267c299](https://github.com/cpenv/tk-cpenv/commit/267c299c8c74acf0fb5b000e27b341c00a768d98) by Dan Bradham).


## [v0.2.0](https://github.com/cpenv/tk-cpenv/releases/tag/v0.2.0) ([compare](https://github.com/cpenv/tk-cpenv/compare/v0.1.2...v0.2.0)) - 2020-05-12

### Added
- Add: modulespecset to maintain multiple versions of a single module ([acfe882](https://github.com/cpenv/tk-cpenv/commit/acfe8820f28f11406ba61e37a2c22524a1021682) by Dan Bradham).
- Add: module_entity and home_path config keys ([29fcb9e](https://github.com/cpenv/tk-cpenv/commit/29fcb9e3563ded8ec820b1cb5ef2a08375517a04) by Dan Bradham).
- Add: dark and light icons ([fa9990d](https://github.com/cpenv/tk-cpenv/commit/fa9990d86c4ceef9bcafab644ac87e3c408c5762) by Dan Bradham).

### Changed
- Change: update ui to group all versions of a module in a single row add: module info panel ([acbe866](https://github.com/cpenv/tk-cpenv/commit/acbe8667a3a14fe2439483c037e98be37b2a1ab8) by Dan Bradham).
- Change: initialize shotgunrepo in init_app this repo is used to find and download modules from shotgun ([ad98099](https://github.com/cpenv/tk-cpenv/commit/ad980997cd997b00aca0306703cb154f1a85389d) by Dan Bradham).
- Change: update cpenv to 0.5.1 ([22a5f46](https://github.com/cpenv/tk-cpenv/commit/22a5f46143a93de3ab00707dc677c55fddd15eaa) by Dan Bradham).

### Fixed
- Fix: activate requires a list rather than single file path ([633fb9a](https://github.com/cpenv/tk-cpenv/commit/633fb9ac28a1fd69a270ae87b5885477fc7e7d5e) by Dan Bradham).


## [v0.1.2](https://github.com/cpenv/tk-cpenv/releases/tag/v0.1.2) ([compare](https://github.com/cpenv/tk-cpenv/compare/v0.1.1...v0.1.2)) - 2020-04-23

### Fixed
- Fix: return resolved modules from activate ([89f7872](https://github.com/cpenv/tk-cpenv/commit/89f7872bb5dde304bdff746928d457ebcb65d6f7) by Dan Bradham).


## [v0.1.1](https://github.com/cpenv/tk-cpenv/releases/tag/v0.1.1) ([compare](https://github.com/cpenv/tk-cpenv/compare/v0.1.0...v0.1.1)) - 2020-04-23

### Added
- Add: example tk-shotgun.yml config - enables tk-cpenv for website ([51f6fd9](https://github.com/cpenv/tk-cpenv/commit/51f6fd96249e3bb55087f9812a03fe64f939ae78) by Dan Bradham).

### Changed
- Change: bump to v0.1.1 ([0199249](https://github.com/cpenv/tk-cpenv/commit/01992497498ae147b6ac03d2c741976428090107) by Dan Bradham).
- Change: update cpenv to 0.4.4 ([5b071af](https://github.com/cpenv/tk-cpenv/commit/5b071aff695fb37f9f083712e32bb011e3497747) by Dan Bradham).

### Fixed
- Fix: use software_entity engine key fallback to engine_name ([4136049](https://github.com/cpenv/tk-cpenv/commit/4136049b8d594c9c9f3caec8b872322868f434b4) by Dan Bradham).


## [v0.1.0](https://github.com/cpenv/tk-cpenv/releases/tag/v0.1.0) ([compare](https://github.com/cpenv/tk-cpenv/compare/98904ad3c2b7fcb8790e7756e78f67c35a74700b...v0.1.0)) - 2020-04-22

### Added
- Add: shotgun desktop preview ([c9161e9](https://github.com/cpenv/tk-cpenv/commit/c9161e9bd0426dccc6a8f5f8d39c4cec5877a172) by Dan Bradham).

### Misc
- Move: config files to example_config ([af381e0](https://github.com/cpenv/tk-cpenv/commit/af381e087d0cfe2ccb66edd90ad704a88ec69083) by Dan Bradham).
- Update readme.md ([10a066e](https://github.com/cpenv/tk-cpenv/commit/10a066ef17cf6db7c80d99e94a323f814fe4c2c5) by Dan Bradham).
- Update label ([b653bf7](https://github.com/cpenv/tk-cpenv/commit/b653bf727234cbbefbb95b067d379a85d4a521fe) by Dan Bradham).
- Initial commit ([98904ad](https://github.com/cpenv/tk-cpenv/commit/98904ad3c2b7fcb8790e7756e78f67c35a74700b) by Dan Bradham).

