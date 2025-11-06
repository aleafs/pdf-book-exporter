source $VIMRUNTIME/vimrc_example.vim 

map <F6> :tabnext<CR>
map <F5> :tabprevious<CR>
map <F3> :tabnew<CR>
map <F9> :make %<<CR>
map gf :tabnew <cfile><CR>

syntax on
filetype on

set paste
set tabstop=4
set softtabstop=4
set shiftwidth=4
set noexpandtab

if has("autocmd")
	autocmd BufNewFile,BufRead *.json set filetype=json
	autocmd BufNewFile,BufRead *.rss set filetype=xml
	autocmd BufNewFile,BufRead *.ejs set filetype=html
	autocmd BufNewFile,BufRead *.go set filetype=go
	autocmd BufNewFile,BufRead *.pac set filetype=pac
	autocmd BufNewFile,BufRead *.cypher set syntax=cypher

	autocmd FileType javascript,json,sql,cypher,php setlocal ts=2 sts=2 sw=2 expandtab
	autocmd FileType java,sh,dosini,html,c,cpp,xml,pac setlocal ts=4 sts=4 sw=4 expandtab
	autocmd FileType go setlocal noexpandtab
endif

set autoindent
set cindent

set foldmethod=marker

set showmatch
set nobackup

if has("persistent_undo")
	set noundofile
endif

set fileencodings=ucs-bom,utf-8,chinese,prc,taiwan,latin-1
set fileencoding=utf-8

set encoding=utf-8
set termencoding=utf-8 
set ffs=unix,dos,mac
set ff=unix

set nocp
set hls

if has('mouse')
	set mouse=v
endif

set columns=180
" set guioptions-=T

set number
set nowrap

" statusline
set laststatus=2
set statusline=%f\ %m%y[%{&ff}:%{&fenc}]\ %5.(%p%%%)\ %20.(\ %l,%c%V%)
