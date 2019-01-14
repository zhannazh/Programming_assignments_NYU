""" This class module generates two types of by-region histograms and one type of boxplots for the given year"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab
import seaborn as sns


class data_analysis:
        
    def __init__(self, data, year):
        """Initiate an instance of the data_analysis class. For each year, plot histograms and boxplots by region"""
        self.year = year
        self.data = data
        
    def histogram_type1(self):
        """Produce a grid of 6 histograms (one per region) where x- and y-axes match """

        # this will show grids at ticks. This style is applied to all plots.
        sns.set(style="whitegrid")
        
        # set x-axis and y-axis limits so that it is easier to compare histograms over time
        g = sns.FacetGrid(self.data, col="Region", col_wrap=3, size=3, xlim=(0, 100000),ylim=(0,0.0005))
        g = g.map(plt.hist, "Income", normed = True, bins=15,color="r")
        g.set_xticklabels(fontsize=10, rotation=30)
        g.set_xlabels("Income per capita",fontsize = 10)
        g.set_ylabels("Distribution",fontsize = 10)
        plt.tight_layout()
        plt.subplots_adjust(top=0.9)
        g.fig.suptitle("Histograms of Income Per Capita in " + str(self.year)+ ", by Region")
        plt.savefig('Histograms for Year ' + str(self.year) +'.pdf')
        pylab.show()

    def histogram_type2(self):
        """Produce one stacked histogram """
        
        bins =10    
        colors = ['r', 'b', 'c', 'y', 'g', 'm']
        labels = ['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America']
        
        # this creates a dataframe with Country index and 6 region columns that contain Income or NaN 
        regional_data = self.data.pivot(index='Country', columns='Region', values='Income')
        
        # prepare data for stacked histogram input
        data_for_hist = [regional_data.AFRICA.dropna(), regional_data.ASIA.dropna(),
                         regional_data.EUROPE.dropna(), regional_data['NORTH AMERICA'].dropna(),
                         regional_data.OCEANIA.dropna(), regional_data['SOUTH AMERICA'].dropna()]
        
        plt.hist(data_for_hist,bins,normed=1, histtype='bar', color=colors, label = labels, stacked=True)
        plt.legend()
        plt.xlabel("Income per capita") 
        plt.ylabel("Distribution")
        plt.title("Stacked Histogram of Income per Capita by Region in " + str(self.year))
        plt.xticks(fontsize=10) 
        plt.yticks(fontsize=10)
        # set x-axis limit so that it is easier to compare histograms over time
        plt.xlim(0, 100000)
        plt.tight_layout()
        plt.savefig('Stacked Histogram for Year ' + str(self.year) +' by Region.pdf')
        pylab.show()        
        
        
    def boxplot(self):
        """Produce one plot with 6 boxplots (one per region) """

        data_for_boxplot=self.data.pivot(index='Country', columns='Region', values='Income')
        # this creates a dataframe with Country index and 6 region columns that contain Income or NaN (the default setting in boxplot automatically drops NaNs)
        
        data_for_boxplot.plot.box(figsize=(10,5))
        plt.title("Boxplots of Income Per Capita \n In " + str(self.year) +", by Region")
        plt.xlabel("Regions")
        plt.ylabel("Income per capita")
        plt.ylim(0, 100000)
        # the upper y-axis limit is set to $100,000 so that it is easier to compare boxplots over time
        plt.savefig('Boxplots for Year ' + str(self.year) +'.pdf')
        pylab.show()
        
  
 