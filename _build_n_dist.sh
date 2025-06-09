rm -rf build/ dist/ *.egg-info **/*.egg-info &>/dev/null
python bump.py


# Including FuseWill in this distribution
src_dir="$(pwd)/olca"
fusewill_src="/b/Dropbox/_jgongery/orpheus/x/477-adequate-tracing/src"
fusewill_files="fusewill_cli.py fusewill_utils.py"
(cd $fusewill_src && for f in $fusewill_files; do (cd $src_dir;if [ -e "$f" ];then git add $f &>/dev/null;git commit $f -m "update:$f"&>/dev/null;chmod 777 $f&>/dev/null;fi);cp $f $src_dir;chmod 555 $src_dir/$f; done)
#(cd $fusewill_src && for f in $fusewill_files; do (cd $src_dir;if [ -e "$f" ];then git add $f &>/dev/null;git commit $f -m "update:$f"&>/dev/null;chmod 777 $f&>/dev/null;fi);cp $f $src_dir;chmod 555 $src_dir/$f; done)
sleep 2

python setup.py sdist bdist_wheel && (twine upload dist/* || pip install twine --quiet && twine upload dist/*)

