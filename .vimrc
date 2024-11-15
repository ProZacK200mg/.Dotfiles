set nocompatible                 "sets vim mode instead of vi
filetype plugin indent on        "enables plugins
syntax enable                    "syntax for all filetypes
set autoindent                   "indents from previous line
set tabstop=4                    "makes tab lenght 4 spots
set hlsearch                     "turns on highlight search
set ignorecase                   "ignores case in search
set smartcase                    "makes sure case doesn't matter when searching
set encoding=utf8                "utf8 incoding
set wrap                         "wraps the line if it runs off screen
set linebreak                    "enables linebreak character
set showbreak=...                "shows ... at the begining of new line break 
set list lcs=tab:>-,trail:-      "shows >- for tabs and - for whitespace
set ruler                        "always shows the cordinace for the ruler in the bottom right
set laststatus=2                 "always shows bottom stat line
set wildmenu                     "menu inside vim
set wildmode=longest:list,full   "how wild menu behaves
set cursorline                   "highlights the line the cursor is on
hi CursorLine ctermbg=8          "makes the highlight background colored
set number relativenumber        "shows line numbers and the number relative to the line you're on
set title                        "shows the window name
set autoread                     "reloads a file that has been written but not modified
set so=10                        "shows 10 lines from top and bottom of screen and all times
set confirm                      "confirm exit on none :wq
set nojoinspaces                 "doesnt add a space when joining lines togeather
set splitbelow splitright        "tabed windows split down then right

"=> key mapping

map <F6>:setlocal spell! spelllang=en_us <CR> "maps search to f6
