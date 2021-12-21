#/bin/sh

file_filter=*.avi

if [ -n "$1" ]; then
  echo "Processing directory: $1"
  process_dir=$1
else
  echo "Directory not supplied."
  exit
fi

# better quality: ffmpeg -i gen-000900.avi -codec:v libtheora -qscale:v 3 -f ogv gen-000900-1.ogv

FILES=`find -L ${process_dir} -name "${file_filter}"`
for file in $FILES
do
    CMD="ffmpeg -i ${file} -codec:v libtheora -qscale:v 1 -f ogv ${file%.*}.ogv"
    echo $CMD
    $CMD
done

