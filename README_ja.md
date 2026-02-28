# mc_remote_samples_practice

Minecraft Remote（マイクラリモコン）のAPIを使いPythonでユーザーコードを書く出発点です

dorahari.131によるmc_remote_samples におけるアイデア及び練習
***
このドキュメントは、Reveal.jsに対応しています。

--

## このリポジトリの内容

現在は巨大な家を建築済み
レイアウトは決めましたが、マイクラ建築初心者のため、
他のワールドで手動建築を行って、家具などの作り方を学んでいる。


--

### README（このファイル）
  - マイクラリモコンの概要
  - シングルプレイワールドの建築
  - 箱庭サーバーの利用方法
  - Python環境準備とデモコードの実行
  - このプログラムにおけるそれぞれの役割

---

PythonコーディングでMinecraft世界に自動建築ができます。
[Minecraft Remote（`McRemote`）プラグイン](https://github.com/Naohiro2g/McRemote)をインストールした[PaperMC](https://papermc.io/)サーバーが必要です。

<img src="https://raw.githubusercontent.com/Naohiro2g/minecraft-remote-api/refs/heads/main/images/mc-remote.png" width="320" alt="Minecraft Remote World" title="Minecraft Remote World" />
ご心配なく。箱庭（サンドボックス）サーバーを利用して、今すぐ、始められます。

***

1.16.5のシングルプレイも可能です←こちらでやってます
（建築が他人の範囲に出るので）

--

# for Minecraft Java Edition 1.16.5
荒らしたくなければ1.16.5ワールドにどうぞプラグイン方法は
from mcje.minecraft import Minecraft
import param_MCJE as param
と
mc = Minecraft.create(port=param.PORT_MC)  # MCJE:14712, MCPI:4711
mc.postToChat("Hello")

---

## 箱庭サーバーに参加してみよう

同じ仕様で家庭、教室などに自分のサーバーを準備すると、より楽しい体験ができるかも。でも、まずは、試してみないとね。

このサーバーは、割と短期間で初期化するので、ちょっとぐらい失敗しても許されます。

***

自分のワールドならいくらでも削除はできます。
commandで消すことも可能。
私は消去用としてaxis_flat.pyを愛用してます。

--

### マインクラフト サーバー情報

名称：「箱庭（サンドボックス）サーバー」

- アドレス
  - `mc-remote.xgames.jp`
- ポート
  - Java版　`25565` （指定不要）
  - Bedrock版　`25565` （指定する）

「ほとんど、どんなクライアントもつながる」仕様

--

### シングルプレイの利点

シングルプレイならコマンドも使えるし管理者権限を使えます。
何回でも作って消せます。
また、他人に迷惑は掛かりません

***
大規模なものを作ったり、サイズ感がわからないのだったら、
一回自分のワールドで試してはどうでしょう

---

### クライアント アプリ（マルチモード）

「ほとんど、何でもつながる」はず

- Java / Fabric / NeoForge / Forge 1.8.8〜最新
- 統合版（iOS / Android / Windowsを含む）
- 推奨セットアップは影mod入りJava版:

    [`Iris`](https://irisshaders.github.io/) / Fabric と [`MakeUp - Ultra Fast`](https://modrinth.com/shader/makeup-ultra-fast-shaders/changelog?l=iris) シェーダー

***
Forgeはモッド導入にお勧め
とくに1.12.2 1.16.5 1.20.1は対応モッド多め

---

## 非常に重要な準備作業

`param_mc_remote.py`のパラメータを編集します。

```python
PLAYER_NAME = "PLAYER_NAME"  # set your player name in Minecraft

PLAYER_ORIGIN = Vec3(2000, 0, 2000)  # PO.x, PO.y, PO.z

ADRS_MCR = "mc-remote.xgames.jp"  # mc-remote sandbox server
PORT_MCR = 25575  # socket server port
```

**APIを利用時に、PLAYER_NAME と同じ名前でMinecraftサーバーに参加していること。**

箱庭サーバーを使うならPLAYER_NAMEだけ変更。
***
シングルプレイでは
`param_MCJE.py`を使ってます。

--

### `PLAYER_ORIGIN` は建築座標系の原点

`PLAYER_ORIGIN` からの相対座標で、ブロックが配置されます。
たとえば、

- `PLAYER_ORIGIN`： `(2000, 0, 2000)`
- コマンド： `setBlock(5, 68, 5, block.GOLD_BLOCK)`

⇒ 結果： `(2005, 68, 2005)` に金ブロック出現
***
変更した後に「どこ？」とならないように覚えておくこと

--

## Discordコミュニティ

Discordコミュニティでは、不明点を質問したり、他のユーザーと経験を共有できます。

箱庭サーバーやAPIの使い方、サーバーの建て方などについて質問がある場合は、[Discordサーバー](https://discord.gg/xUqhhqWsuS)内の `mc-remote-chat` チャンネルをご利用ください。
***
Discordの機能がいまいちわかっていないので専門家さん使い方のレクチャーをお願いします。

---

## 環境の準備と更新

--

- とにかく試したい人向けの最短手順
- Python環境を最初から構築する手順
  - Python 3.10から3.12
  - pyenvによるPythonインストール
  - poetryによるプロジェクト内への仮想環境生成
- クライアント / APIを準備
  - [minecraft-remote-api @ Pypi.org](https://pypi.org/project/minecraft-remote-api/)

--

#### Pythonだけで勝負！の場合

このリポジトリのクローンさえ不要、PLAYER_NAMEを自分のプレイヤー名に書き換えるだけ。Thonnyなんかもいいね。mu-editorは、Python 3.8で止まっているので無理。

```bash
# パッケージをインストール／更新
pip install minecraft-remote-api -U

# ファイルに保存するか、REPLモードで
import mc_remote.minecraft import Minecraft
mc = Minecraft.create("mc-remote.xgames.jp", 25575)
mc.setPlayer("PLAYER_NAME", 2000, 0, 2000)
mc.postToChat("Hello, hello!")
mc.setBlock(5, 68, 5, "gold_block")
```
***
これ忘れると何もできないのでスクショを

--

#### とくかく、試したいのだ、という場合

Python 3.10から3.12があるなら、以下の要領で。

```bash
# パッケージをインストール／更新
pip install minecraft-remote-api -U

# examples/param_mc_remote.pyを編集して、自分のプレイヤー名に変更。
# PLAYER_NAME = "PLAYER_NAME"

# hello, world!
cd examples
python hello.py
```

---

### 推奨するPython環境構築

- pyenvをインストール
- pyenvでPythonをインストール
- poetryをインストール

--

Pythonパッケージの最新版は [PyPI](https://pypi.org/project/minecraft-remote-api/) からインストールできます。

#### pyenv / poetryがインストールされている場合

```bash
poetry install


# 仮想環境(.venv/)が作成されたのを確認し、今後は、その環境内で作業してください。
```

パッケージを更新するには、次のコマンドを実行:

```bash
poetry update
```

--

#### pyenv / poetryがインストールされていない場合

Python 3.9以上がインストールされていることを確認して、次のコマンドを実行:

```bash
pyenv local 3.11.9  # もし、pyenvをインストール済みなら
pip install minecraft-remote-api
```

（現在は、Python 3.11.9, 3.12.10が推奨です。）

パッケージを更新するには、次のコマンドを実行:

```bash
pip install minecraft-remote-api -U
```

パッケージ管理のためにpyenv / poetryを使うことをオススメします。少なくとも、pyenvを使うとPythonのバージョン管理が楽になります。

pyenv / poetryのインストール方法は、[こちら](https://github.com/Naohiro2g/minecraft-remote-api/docs/pyenv_and_poetry_ja.md)を参照してください。


---

### バグ集

#### なぜか「かける」が機能しない

これはよくわからない

#### pythonのlocal,grobalが機能しない

このパソコンの仕様のようで対策しても変化なし

--

### アイデア集

チェス

家

暗号

--

### flippy.pyを応用し、チェスや将棋、オリジナルゲームを作る
***
オリジナルゲームはチェスや、将棋などを応用し、マイクラモブの新作ボードゲームを作る


--

### 簡単な暗号伝達
#### It Kids の古い用紙を捜索済み
昔IT算数の授業で行った暗号づくりの方法をコマンドにまとめ、液晶のように横流し表示を目指す
***
暗号方法は見つかったもの、機械としての判断は設定するしかなさそうなのでほかの方法を試す

できればエニグマ暗号みたいに高度なものを目指す

--

### 家を作るための階段や部屋を作るコマンドを作る
#### 実行中
会談と部屋はほぼできているので、螺旋階段や、家具などを模索中
***
大きな家を1.16.5に制作中　階段と大まかな部屋は構築済み
螺旋階段はコマンドのための建築中

---

## 現在の進捗状況と解説

`kadai_11.py`
における進捗状況

---

###　リセット

リセットは
```python
mc.setBlocks(-90, param.Y_SEA + 1, -90,   -2, param.AXIS_TOP,    -2,    param.AIR)
```
で空気に置き換えることで実行

---

###　屋根

屋根は
```python
#setLoof
mc.postToChat('set Loof')
rx=-84, ry=19, rz=-84, rs=79
setPyramid(x=rx, z=-rz, y=param.Y_SEA + ry, size=rs, blockTypeId=param.IRON_BLOCK)
setPyramid(x=rx+1, z=-rz+1, y=param.Y_SEA + ry, size=rs-2, blockTypeId=param.SHROOMLIGHT)
setPyramid(x=rx+2, z=-rz+2, y=param.Y_SEA + ry, size=rs-4, blockTypeId=param.AIR)
```
で設置

---

### フロア

階層は
```python
#setFloor
mc.postToChat('set Floor')
sleep(0.01)
mc.postToChat('set 1st Floor')
fsx=81,fsy=1,fsz=81,ffx=9,ffy=10,ffz=9
mc.setBlocks(-fsx, param.Y_SEA + fsy, -fsz,   -ffx,  param.Y_SEA+ffy,      -ffz,     param.IRON_BLOCK)
mc.setBlocks(-fsx+2, param.Y_SEA + fsy+1, -fsz+2,   -ffx-2, param.Y_SEA+ffy-1,      -ffz-2,    param.AIR)
sleep(0.01)

mc.postToChat('set 2nd Floor')
mc.setBlocks(-fsx, param.Y_SEA + fsy+10, -fsz,   -ffx, param.Y_SEA+ffy+10,    -ffz,     param.IRON_BLOCK)
mc.setBlocks(-fsx+2, param.Y_SEA + fsy+11, -fsz+2,   -ffx-2, param.Y_SEA+ffy+9,    -ffz-2,    param.AIR)
sleep(0.01)

mc.postToChat('set 3rd Floor')
mc.setBlocks(-fsx+9, param.Y_SEA + fsy+20, -fsz+9,   -ffx-9, param.Y_SEA+ffy+20,    -ffz-9,    param.IRON_BLOCK)
mc.setBlocks(-fsx+11, param.Y_SEA + fsy+21, -fsz+11,   -ffx-11, param.Y_SEA+ffy+19,    -ffz-11,    param.AIR)
sleep(0.01)

mc.postToChat('set 4th Floor')
mc.setBlocks(-fsx+18, param.Y_SEA + fsy+30, -fsz+18,   -ffx-18, param.Y_SEA+ffy+30,    -ffz-18,    param.IRON_BLOCK)
mc.setBlocks(-fsx+20, param.Y_SEA + fsy+31, -fsz+20,   -ffx-20, param.Y_SEA+ffy+29,    -ffz-20,    param.AIR)
sleep(0.01)

mc.postToChat('set 5th Floor')
mc.setBlocks(-fsx+27, param.Y_SEA + fsy+40, -fsz+27,   -ffx-27, param.Y_SEA+ffy+40,    -ffz-27,    param.IRON_BLOCK)
mc.setBlocks(-fsx+29, param.Y_SEA + fsy+41, -fsz+29,   -ffx-29, param.Y_SEA+ffy+39,    -ffz-29,    param.AIR)
sleep(0.01)
```
で設置

---

### 一階の部屋
一階の部屋は
```python
#setRoom
mc.postToChat('set Room')
mc.postToChat('set Room on first floor')
setRoom(x=-10, z=-10, y=param.Y_SEA + 1, sizex=9,  sizey=9, sizez=5,  blockTypeId=param.IRON_BLOCK)
setRoom(x=-20, z=-10, y=param.Y_SEA + 1, sizex=55, sizey=9, sizez=5,  blockTypeId=param.SMOOTH_QUARTZ)
setRoom(x=-76, z=-10, y=param.Y_SEA + 1, sizex=4,  sizey=9, sizez=5,  blockTypeId=param.IRON_BLOCK)
setRoom(x=-10, z=-21, y=param.Y_SEA + 1, sizex=14, sizey=9, sizez=20, blockTypeId=param.SMOOTH_QUARTZ)
sleep(0.01)
setRoom(x=-25, z=-21, y=param.Y_SEA + 1, sizex=9,  sizey=9, sizez=9,  blockTypeId=param.IRON_BLOCK)
setRoom(x=-35, z=-21, y=param.Y_SEA + 1, sizex=9,  sizey=9, sizez=9,  blockTypeId=param.IRON_BLOCK)
setRoom(x=-45, z=-21, y=param.Y_SEA + 1, sizex=14, sizey=9, sizez=14, blockTypeId=param.IRON_BLOCK)
setRoom(x=-60, z=-21, y=param.Y_SEA + 1, sizex=20, sizey=9, sizez=20, blockTypeId=param.SMOOTH_QUARTZ)
sleep(0.01)
setRoom(x=-25, z=-31, y=param.Y_SEA + 1, sizex=9,  sizey=9, sizez=10, blockTypeId=param.SMOOTH_QUARTZ)
setRoom(x=-35, z=-31, y=param.Y_SEA + 1, sizex=9,  sizey=9, sizez=10, blockTypeId=param.SMOOTH_QUARTZ)
setRoom(x=-45, z=-36, y=param.Y_SEA + 1, sizex=14, sizey=9, sizez=5,  blockTypeId=param.IRON_BLOCK)
setRoom(x=-10, z=-47, y=param.Y_SEA + 1, sizex=15, sizey=9, sizez=27, blockTypeId=param.SMOOTH_QUARTZ)
sleep(0.01)
setRoom(x=-10, z=-75, y=param.Y_SEA + 1, sizex=15, sizey=9, sizez=5,  blockTypeId=param.SMOOTH_QUARTZ)
setRoom(x=-26, z=-47, y=param.Y_SEA + 1, sizex=20, sizey=9, sizez=33, blockTypeId=param.SMOOTH_QUARTZ)
setRoom(x=-47, z=-47, y=param.Y_SEA + 1, sizex=33, sizey=9, sizez=6,  blockTypeId=param.IRON_BLOCK)
setRoom(x=-47, z=-54, y=param.Y_SEA + 1, sizex=33, sizey=9, sizez=6,  blockTypeId=param.IRON_BLOCK)
sleep(0.01)
setRoom(x=-47, z=-61, y=param.Y_SEA + 1, sizex=33, sizey=9, sizez=6,  blockTypeId=param.IRON_BLOCK)
setRoom(x=-47, z=-68, y=param.Y_SEA + 1, sizex=33, sizey=9, sizez=6,  blockTypeId=param.IRON_BLOCK)
setRoom(x=-47, z=-74, y=param.Y_SEA + 1, sizex=22, sizey=9, sizez=6,  blockTypeId=param.IRON_BLOCK)
setRoom(x=-70, z=-74, y=param.Y_SEA + 1, sizex=10, sizey=9, sizez=6,  blockTypeId=param.SMOOTH_QUARTZ)
sleep(0.01)
mc.setBlocks(-72, param.Y_SEA + 2, -76, -79, param.Y_SEA + 7, -79, param.DIAMOND_BLOCK)
sleep(0.01)
```
で設置

---

### 二階の部屋

二階の部屋は
```python
mc.postToChat('set Room on second floor')
setRoom(x=-10, z=-66, y=param.Y_SEA + 11, sizex=20, sizey=9, sizez=14, blockTypeId=param.SMOOTH_QUARTZ)
setRoom(x=-10, z=-10, y=param.Y_SEA + 11, sizex=29, sizey=9, sizez=27, blockTypeId=param.IRON_BLOCK)
setRoom(x=-10, z=-38, y=param.Y_SEA + 11, sizex=29, sizey=9, sizez=27, blockTypeId=param.IRON_BLOCK)
setRoom(x=-10, z=-10, y=param.Y_SEA + 11, sizex=34, sizey=9, sizez=27, blockTypeId=param.IRON_BLOCK)
sleep(0.01)
setRoom(x=-45, z=-10, y=param.Y_SEA + 11, sizex=33, sizey=9, sizez=27, blockTypeId=param.IRON_BLOCK)
setRoom(x=-40, z=-38, y=param.Y_SEA + 11, sizex=40, sizey=9, sizez=42, blockTypeId=param.SMOOTH_QUARTZ)
setRoom(x=-31, z=-70, y=param.Y_SEA + 11, sizex=8,  sizey=9, sizez=10, blockTypeId=param.IRON_BLOCK)
sleep(0.01)
```
で設置

---

### 三階以降は小さくなるため、レイアウトはまだ決めてません

というか三階からは大部屋としての利用を検討しています

---

### 床

床は
```python
#setFlooring
mc.postToChat('set Flooring')
mc.setBlocks(-79, param.Y_SEA + 1, -79,   -11, param.Y_SEA+1,    -11,    param.SHROOMLIGHT)
sleep(0.01)
mc.setBlocks(-79, param.Y_SEA + 11, -79,   -11, param.Y_SEA+11,    -11,    param.SHROOMLIGHT)
sleep(0.01)
mc.setBlocks(-79, param.Y_SEA + 21, -79,   -11, param.Y_SEA+21,    -11,    param.SHROOMLIGHT)
sleep(0.01)
mc.setBlocks(-71, param.Y_SEA + 31, -71,   -19, param.Y_SEA+31,    -19,    param.SHROOMLIGHT)
sleep(0.01)
mc.setBlocks(-62, param.Y_SEA + 41, -62,   -28, param.Y_SEA+41,    -28,    param.SHROOMLIGHT)
sleep(0.01)
```
で設置

---

### 階段

階段は
```python
#setStep
mc.postToChat('set steps')
setStep(x=-16, z=-79,y=param.Y_SEA +2, size=4, high=10, blockTypeId=param.SHROOMLIGHT)
sleep(0.01)
setStep(x=-20, z=-70,y=param.Y_SEA +11, size=4, high=10, blockTypeId=param.SHROOMLIGHT)
sleep(0.01)
setStep(x=-29, z=-61,y=param.Y_SEA +21, size=4, high=10, blockTypeId=param.SHROOMLIGHT)
sleep(0.01)
setStep(x=-38, z=-52,y=param.Y_SEA +31, size=4, high=10, blockTypeId=param.SHROOMLIGHT)
sleep(0.01)
```
で設置

--

### ここで使った工夫

--

## 工夫①
#### setstep

---

### 階段設置の簡素化
setstepというコマンドは
```python
def setStep(mc=mc, x=0, z=0, y=param.Y_SEA + 1, size=3, high=3,  blockTypeId=param.IRON_BLOCK):
    # inclination = 1/n or n
    # ChangeX = 1 or -1
    size -= 1
    mc.setBlocks(x, y + high - 1, z, (x - high) + 1, y + high, z + size, param.AIR)
    mc.setBlocks(x, (y + high) - 2, z, (x - high) + 2, (y + high) - 1, z + size, param.AIR)
    while high > 0:
        mc.setBlocks(x, y, z, x, y, z + size, blockTypeId)
        x -= 1
        high -= 1
        y += 1
        sleep(0.01)
```
で設定

---

### 改善点

```python
def setStepX(mc=mc, x=0, z=0, y=param.Y_SEA + 1, size=3, high=3, inclination=1, Changex=-1,  blockTypeId=param.IRON_BLOCK):
    # inclination = 1/n or n
    # ChangeX = 1 or -1
    while high > 0:
        ny = inclination
        nx = 1 // inclination
        mc.setBlocks(x, y, z, x, y, z + size, blockTypeId)
        x += nx ** Changex
        high -= ny
        y += ny
        sleep(0.01)
```
で分かるように、現在傾きを含めた設置を模索中だが、「かける」ができないため一時中断中

--

## 工夫②
#### setRoom

---

### 部屋の設置の簡略化

setRoomというコマンドは
```python
def setRoom(mc=mc, x=0, z=0, y=param.Y_SEA + 1, sizex = 1,sizey = 1,sizez = 1, blockTypeId=param.IRON_BLOCK):
    mc.setBlocks(x, y, z, x - sizex, y + sizey, z - sizez, blockTypeId)
    mc.setBlocks(x - 1, y + 1, z - 1, x - sizex + 1, y + sizey - 1, z - sizez + 1, param.AIR)
    sleep(0.01)
```
で設定

--

## ご清聴ありがとうございました
***
***