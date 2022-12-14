# Spoticasso

> Spotify playlist 커버 이미지 자동 생성 웹서비스

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

음악 플레이리스트 공유가 유행함에 따라, spotify 플레이리스트를 분석하여 커버 이미지를 자동으로 생성해주는 웹 서비스 입니다. 

![create_image](https://user-images.githubusercontent.com/66311161/202813170-d476ddb5-2d56-47de-9343-27a1da4d80e0.jpeg)

사용자는 웹 브라우저를 통해 spotify에 로그인 할 수 있으며, 로그인에 성공한 경우 시스템은 사용자의 플레이리스트 목록을 불러오고 사용자는 원하는 플레이리스트를 선택하여 커버 이미지를 생성합니다. 시스템은 자연어 처리 모델을 이용해 플레이리스트를 분석하고 번역해 주요 키워드를 추출합니다. 추출된 키워드는 딥러닝 텍스트-이미지 모델을 틍해 적절한 그림을 생성합니다. 생성된 이미지는 자동으로 spotify 플레이리스트 커버 이미지로 등록됩니다.

## Sample Image

- playlist_dance

<img width="30%" align="left" src="https://user-images.githubusercontent.com/66311161/202968694-a02831fd-e69f-4b45-9a78-0d0a8873a550.png" />
<img width="30%" src="https://user-images.githubusercontent.com/66311161/202968724-898d707e-dffe-4b12-a116-d9186404744d.png" />

- playlist_trot

<img width="30%" align="left" src="https://user-images.githubusercontent.com/66311161/202968757-dcb98634-d178-465b-8a3b-e7ddf3789dae.png" />
<img width="30%" src="https://user-images.githubusercontent.com/66311161/202968806-5d6430bd-8e19-4a2f-a075-f41033860dfe.png" />


- playlist_indie

<img width="30%" align="left" src="https://user-images.githubusercontent.com/66311161/202968814-4df8f33f-7590-408e-95c8-b78791e2d091.png" />
<img width="30%" src="https://user-images.githubusercontent.com/66311161/202968819-9ecb5ba8-bcee-49b0-8df1-b0102a77e328.png" />

## Tech Usage


* Python 3.8.15
* Django 4.1
* KeyBert 0.7.0
* requests 2.28.0
* spotipy 2.21.0
* replicate 0.4.0
* googletrans 4.0.0
* Bootstrap 5.2

## Start

1. [Playlist.py](https://github.com/dvpaa/spoticasso/blob/main/spoticasso/spoticassoapp/Playlist.py)에 사용자의 cid와 csc를 입력합니다.  
2. stable-diffusion [api token](https://replicate.com/docs)을 발급 후 환경변수 설정을 합니다.
  ```sh
  export REPLICATE_API_TOKEN = <TOKEN>  
  ```  
3. library 설치

  Terminal
  
  ```sh
  cd spoticasso/spoticassoapp
  pip install -r requirements.txt
  cd ../
  python manage.py runserver
  ```

## Release History

- 1.0.0
  - First Release : 2022 AmPm 4th Hackathon
  
 ## Contributors
 
 - Han Subin [subinhan](https://github.com/subinhan)
 - Kim Jaehyeon [kiku99](https://github.com/kiku99)
 - Kim Geonu [dvpaa](https://github.com/dvpaa)
 - Kim Yuna [yuna47](https://github.com/yuna47)

## ScreenShot

  <img width="1440" alt="index" src="https://user-images.githubusercontent.com/66311161/202812902-81fce605-a92f-43a1-8be9-8e3625c1cfb1.png">
  <img width="1440" alt="select" src="https://user-images.githubusercontent.com/66311161/202813033-2e44af7c-4804-4ef0-a3bb-e0d69ad980f8.png">
  <img style="display:block; margin:auto; width:480;" src="https://user-images.githubusercontent.com/82706622/202822306-017ec098-de18-4f66-94f0-63dc6485c46a.jpeg">
  
 <!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/ampm-jbnu/JBNU-SE-Voting.svg?style=flat-square
[contributors-url]: https://github.com/ampm-jbnu/JBNU-SE-Voting/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ampm-jbnu/JBNU-SE-Voting.svg?style=flat-square
[forks-url]: https://github.com/ampm-jbnu/JBNU-SE-Voting/network/members
[stars-shield]: https://img.shields.io/github/stars/ampm-jbnu/JBNU-SE-Voting.svg?style=flat-square
[stars-url]: https://github.com/ampm-jbnu/JBNU-SE-Voting/stargazers
[issues-shield]: https://img.shields.io/github/issues/ampm-jbnu/JBNU-SE-Voting.svg?style=flat-square
[issues-url]: https://github.com/ampm-jbnu/JBNU-SE-Voting/issues
 




