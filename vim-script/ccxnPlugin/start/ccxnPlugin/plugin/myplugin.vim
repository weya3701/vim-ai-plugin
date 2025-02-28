" myplugin.vim

function! CallAI(stpe="")
    let arg = getline(1, '$')
    let cmd = "python " . g:AIapis . '"' . join(arg, ',') . '"'
    let res = system(cmd) 
    if a:stpe == "newpage"
        tabnew
        setlocal buftype=nofile
        setlocal bufhidden=hide
        call append(0, split(res, "\n"))
    else
        call append("$", "")
        call append("$", "")
        call append("$", "========================================================")
        call append("$", "AI回覆: ")
        call append("$", split(res, "\n"))
    endif
endfunction

function! CallAIanalysis(stpe="", prompt="", put=0)
    if visualmode() == ""
        echo "請先選取文字"
        return
    endif
    
    execute "'<,'>yank a"
    let content = getreg('a') 

    let arg = a:prompt . "\n" . content 

    let cmd = "python " . g:AIapis . '"' . join(arg, ',') . '"'
    let res = system(cmd) 
    if a:stpe == "newpage"
        tabnew
        setlocal buftype=nofile
        setlocal bufhidden=hide
        call append(0, split(res, "\n"))
    else
        call append("$", "")
        call append("$", "")
        call append("$", "========================================================")
        call cursor(str2nr(a:put), 1)
        call append(str2nr(a:put), "AI回覆: ")
        call append(str2nr(a:put)+1, split(res, "\n"))
    endif
endfunction

command! AI call CallAI()
command! AInewpage call CallAI("newpage")
command! AIanalysis call CallAIanalysis("newpage", "", 0)
command! -nargs=1 AIanalysis call CallAIanalysis("newpage", <f-args>, 0)
command! -nargs=+ AIanalysisMainpage call CallAIanalysis("mainpage", <f-args>)
command! -nargs=+ AIanalysisContent call CallAIanalysis("mainpage", "", <f-args>)
