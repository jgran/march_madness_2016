#!/bin/bash

if [ ! -d fig ]
then
  mkdir fig
fi

python make_season_avg.py
python make_training_dataset.py
python make_plots.py
python make_testing_dataset.py
python make_predictions.py
