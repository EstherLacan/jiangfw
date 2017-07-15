find . -iname '*.jar' -print | while read jar; do
  unzip -qq -l $jar | sed 's/.* //' | while read cls; do
    unzip -c $jar $cls | grep -nq $1 && echo  "$jar:"$cls
  done
done
