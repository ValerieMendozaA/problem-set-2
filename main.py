'''
- You will run Problem Set 2 from this .py, so make sure to set things up to return outputs accordingly
- Go through each PART and write code / make updates as necessary to produce all required outputs
- Run main.py before you start
'''

import src.part1_etl as part1
import src.part2_plot_examples as part2
import src.part3_bar_hist as part3
import src.part4_catplot as part4
import src.part5_scatter as part5

def main():
   ##  PART 1: ETL  ##
    # ETL the datasets into dataframes
    directories = ['data/part2_plots', 'data/part3_plots', 'data/part4_plots', 'data/part5_plots'] 
       part1.create_directories(directories)  pred_universe, arrest_events, charge_counts, charge_counts_by_offense = part1.extract_transform()
    
  ##  PART 2: PLOT EXAMPLES  ## 
   # Apply plot theme
     part2.seaborn_settings()
       part2.barplots(charge_counts, charge_counts_by_offense)
          part2.cat_plots(charge_counts, pred_universe)  
             part2.histograms(pred_universe)
                   part2.scatterplot(pred_universe)

    ##  PART 3: BAR PLOTS AND HISTOGRAMS  ## 
    part3.bar_plot(charge_counts)  
       part3.histogram(pred_universe['some_numeric_column'])  
          part3.bar_plot_by_offense(charge_counts_by_offense)  part3.histogram_with_bins(pred_universe['some_numeric_column'], bins=20)  

   ##  PART 4: CATEGORICAL PLOTS  ## 
    part4.count_plot(charge_counts)  
       part4.box_plot(pred_universe, category='category_column', value='numeric_value_column') 
          part4.violin_plot(pred_universe, category='category_column', value='numeric_value_column')

    ##  PART 5: SCATTERPLOTS  ##
    part5.scatter_basic(pred_universe, x='x_column', y='y_column')
          part5.scatter_with_hue(arrest_events, x='x_column', y='y_column', hue='category_column') 

if __name__ == "__main__":
    main()
