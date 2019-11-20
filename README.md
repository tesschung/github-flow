# Github Flow

```bash
$ git config --global user.name tesschung
$ git config --global user.email geobera0910@naver.com
```



1. repository init
   ```bash
   - master
   git remote add origin `주소`$ git init
   $ git remote add origin https://github.com/tesschung/github-flow.git
   $ git remote -v
   origin  https://github.com/tesschung/github-flow.git (fetch)
   origin  https://github.com/tesschung/github-flow.git (push)
   
   $ git add .
   $ git commit -m "Initial Commit"
   $ git push origin master
   ```

   ```bash
   - slave
   1) master의 repository를 fork
   2) fork한 repository를 복사해서 git clone `주소`
   ```