rm -rf build/ dist/ *.egg-info **/*.egg-info &>/dev/null




python setup.py sdist bdist_wheel  && cdist=$(realpath dist/*whl) && \
	(cd /w/TST/tstolca &&  (conda activate tstolca && (pip uninstall olca -y &>/dev/null;pip install $cdist --quiet )) ) && \
	echo "Installed $cdist in tstolca" || echo "Failed to install $cdist in tstolca"
	


