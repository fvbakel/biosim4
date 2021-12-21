#/bin/sh

BASEDIR=$(dirname "$0")
if [ -n "$1" ]; then
  echo "Storing results in directory: $1"
  results_dir=$1
else
  echo "Directory not supplied."
  exit
fi

/usr/bin/gnuplot --persist ${BASEDIR}/graphlog.gp

mkdir -p ${results_dir}

cp ${BASEDIR}/../biosim4.ini ${results_dir}/
cp ${BASEDIR}/../logs/epoch-log.txt ${results_dir}/
cp ${BASEDIR}/../images/* ${results_dir}/

# convert to ogv files for chromium
${BASEDIR}/avi2ogg.sh ${results_dir}

# make svg files
python3 ${BASEDIR}/graph-nnet.py -d ${results_dir}

# make the html report
python3 ${BASEDIR}/make_html_report.py -d ${results_dir}
