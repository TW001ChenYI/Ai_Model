# 本文說明，本專案係德明財經科技大學-AI二甲的AI人工智慧課程期末考工程「金庸武俠小說產生器」之說明文件

### 作者:陳羿翰

## 目錄
* [設計起源](#設計啟源)
* [發現問題](#發現問題)
* [系統目標](#系統目標)
* [API服務架構](#API服務架構)
* [實測結果](#實測結果)
* [評量結果](#評量結果)
* [硬體資源](#硬體資源)
* [架構圖](#架構圖)

## <a id="設計啟源" />設計起源

### 期末考題型:
1. 模型自行尋找2本金庸小說，並加入訓練。
1. 修改後端超參數
1. 新增前端網業功能為「**生成字數**」及＿**生成溫度**」，可自行設定，最後優化版面設計。

盧老師宣布考題後，當時老師還在講解題目內容的同時，我其實就已經完成了，

## 發現問題
這次的工程裡花了最久的應該是，尋找另外2本金庸小說，因為在網路上不是要註冊會員，就是都是分開章節，找到之後，又有處理字體及一些贅字。
在撰寫此專案時，HTML前端一直ERROR，就發現是我自己少打「"」，真是不小心!
最後，在處理後端接收時，新增函數參數時，出現了資料型態的問題，當下就在函數裡強制轉換，實測結果就完成了。


## <a id="系統目標">系統目標
希望可以在虛擬機下完成，不僅可以減少電腦的負荷量，也可以處理比較大的工程。

## <a id="API服務架構">API服務架構
使用PYTHON中的Flask套件，架設API做為接收器，再利用HTML前端給使用者輸入參數，來完成前後端的連接。

## <a id="實測結果">實測結果
已完成老師交代的功能，並以測試多次沒問題。

- [x] 模型自行尋找2本金庸小說，並加入訓練。
- [x] 修改後端超參數
- [x] 新增前端網業功能為「**生成字數**」及「**生成溫度**」，可自行設定，最後優化版面設計。

## <a id="評量結果">評量結果
在2021/06/21的期末考1對1問答時，我是第二個跟盧老師做問答的，所以在詢問問題，很多都是憑著自己的實力在回答，最後在盧老師，的詢問下，順利通關。

## 硬體資源
* 作業系統:Windows(虛擬機)
* CPU:
* RAM:

## 架構圖

## Emphasis

*This text will be italic*  
_This will also be italic_

**This text will be bold**  
__This will also be bold__

_You **can** combine them_

### Ordered

1. Item 1
1. Item 2
1. Item 3
  1. Item 3a
  1. Item 3b

## Images

![This is a alt text.](/image/sample.png "This is a sample image.")

## Links

You may be using [Markdown Live Preview](https://markdownlivepreview.com/).

## Blockquotes

> Markdown is a lightweight markup language with plain-text-formatting syntax, created in 2004 by John Gruber with Aaron Swartz.
>
>> Markdown is often used to format readme files, for writing messages in online discussion forums, and to create rich text using a plain text editor.

## Tables

| Left columns  | Right columns |
| ------------- |:-------------:|
| left foo      | right foo     |
| left bar      | right bar     |
| left baz      | right baz     |

## Blocks of code

```
let message = 'Hello world';
alert(message);
```

## Inline code

This web site is using `markedjs/marked`.
