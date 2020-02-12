#!/bin/bash
cp ~/rpp/MIVISION/rali/include/node_$1_PS.h ~/rpp/MIVISION/rali/include/node_$1_PD.h
cp ~/rpp/MIVISION/rali/source/node_$1_PS.cpp ~/rpp/MIVISION/rali/source/node_$1_PD.cpp
sed -i 's/PSNode/PDNode/g' ~/rpp/MIVISION/rali/include/node_$1_PD.h
sed -i 's/PSNode/PDNode/g' ~/rpp/MIVISION/rali/source/node_$1_PD.cpp
#sed -i 's/node_$1_PS.h/node_$1_PD.h/g' ~/rpp/MIVISION/rali/source/node_$1_PD.cpp
