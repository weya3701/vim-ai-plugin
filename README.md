# vim-ai-plugin


## 環境

* 確認作業環境必須包含Vi IMProved 9.1且需支援python3
    
        可透過 
            vim --version 
        可確認版本及支援度

## 安裝

* * *

* 複製apis目錄到作業系統環境使用者任意目錄

* 複製vim-script/ccxnPlugin目錄到~/.vim/pack/目錄下

* 設定.vimrc檔案，並新增參數

        let g:AIapis = "<apis目錄>run2.py"

## 操作模式

* 整頁模式(本頁)：指令→ :AI，輸入命令後直接整頁送到API並直接返回結果於頁尾。

* 整頁模式(新分頁)：指令→ :AInewpage，輸入命令後直接整頁送到API並直接返回結果於新分頁。

* 段落模式(新分頁)：指令→ :AIanalysis，在頁面中選取片段後輸入指令，會將已選取片段送到API並返回新分頁。

* 段落模式(本頁)：指令→ :AIanalysisMainpage+<line number>，在頁面中選取片段後輸入指令加上結果返回行號，會將已選取片段送到API並返回本頁中的指定行號。

* 段落提示模式(新分頁)：指令→ :AIanalysis + <提示詞>，在頁面中選取片段後輸入指令加上提示詞，會將已選取片段送到API並返回新分頁。

* 段落提示模式(本頁)：指令→ :AIanalysis + <提示詞>+<line number>，在頁面中選取片段後輸入指令加上提示詞及行號，會將已選取片段送到API並返回結果於本頁指定行號。
