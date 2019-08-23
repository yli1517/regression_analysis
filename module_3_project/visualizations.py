"""
This module is for your final visualization code.
One visualization per hypothesis question is required.
A framework for each type of visualization is provided.
"""

import matplotlib.pyplot as plt
import seaborn as sns

# Set specific parameters for the visualizations
LARGE = 22
MED = 16
SMALL = 12
PARAMS = {'axes.titlesize': LARGE,
          'legend.fontsize': MED,
          'figure.figsize': (16, 10),
          'axes.labelsize': MED,
          'xtick.labelsize': MED,
          'ytick.labelsize': MED,
          'figure.titlesize': LARGE}
plt.rcParams.update(PARAMS)
plt.style.use('seaborn-whitegrid')
sns.set_style("white")


def overlapping_density(package=None, input_vars=None, target_vars=None):
    """
    Set the characteristics of your overlapping density plot
    All arguments are set to None purely as a filler right now

    Function takes package name, input variables(categories), and target
    variable as input.
    Returns a figure

    Should be able to call this function in later visualization code.

    PARAMETERS

    :param package:        should only take sns or matplotlib as inputs, any
                           other value should throw and error
    :param input_vars:     should take the x variables/categories you want to
                           plot
    :param target_vars:    the y variable of your plot, what you are comparing
    :return:               fig to be enhanced in subsequent visualization
                           functions
    """

    # Set size of figure
    fig = plt.figure(figsize=(16, 10), dpi=80)
    color = ['red', 'blue', 'green']
    # Starter code for figuring out which package to use
    if package == "sns":
        for i, cat in enumerate(input_vars):
            sns.kdeplot(target_vars[i], legend=True, lw=5, c=color[i],
                        shade=True, label=cat.title())
    elif package == 'matplotlib':
        for i, cat in enumerate(input_vars):
            plt.hist(target_vars[i], label=cat, linewidth=3, figure=fig)
    else:
        raise Exception('Not a valid plotting package.')

    return fig


def boxplot_plot(package=None, input_vars=None, target_vars=None):
    """
    Same specifications and requirements as overlapping density plot

    Function takes package name, input variables(categories), and target
    variable as input.
    Returns a figure

    PARAMETERS

    :param package:        should only take sns or matplotlib as inputs, any
                           other value should throw and error
    :param input_vars:     should take the x variables/categories you want to
                           plot
    :param target_vars:    the y variable of your plot, what you are comparing
    :return:               fig to be enhanced in subsequent visualization
                           functions
    """
    pass



def visualization_one1(
        target_vars=None,
        input_vars=None,
        output_image_name='h1_visualization'):
    """
    The visualization functions are what is used to create each individual
    image.
    The function should be repeatable if not generalizable
    The function will call either the boxplot or density plot functions you
    wrote above

    :param target_var:
    :param input_vars:
    :param output_image_name: the desired name for the image saved
    :return: outputs a saved png file and returns a fig object for testing
    """
    ###
    fig = overlapping_density(package='sns', input_vars=input_vars,
                              target_vars=target_vars)
    ###

    # Starter code for labeling the image
    plt.xlabel('Annual Payout', figure=fig)
    plt.ylabel('Relative Frequency', figure=fig)
    plt.title('Annual Payout by Gender of Business Owner', figure=fig)
    plt.legend()

    # exporting the image to the img folder
    plt.savefig(f'img/{output_image_name}.png', transparent=True, figure=fig)
    return fig


# please fully flesh out this function to meet same specifications of
# visualization one

def visualization_two2(
        target_vars=None,
        input_vars=None,
        output_image_name='h2_visualization'):
    """
    The visualization functions are what is used to create each individual
    image.
    The function should be repeatable if not generalizable
    The function will call either the boxplot or density plot functions you
    wrote above

    :param target_var:
    :param input_vars:
    :param output_image_name: the desired name for the image saved
    :return: outputs a saved png file and returns a fig object for testing
    """

    fig = overlapping_density(package='sns', input_vars=input_vars,
                              target_vars=target_vars)

    # Starter code for labeling the image
    plt.xlabel('Number of Employees Hired', figure=fig)
    plt.ylabel('Relative Frequency', figure=fig)
    plt.title('Number of Employees Hired by Gender of Business Owner',
              figure=fig)
    plt.legend()

    # exporting the image to the img folder
    plt.savefig(f'img/{output_image_name}.png', transparent=True, figure=fig)
    return fig


def visualization_three3(
        target_vars=None,
        input_vars=None,
        output_image_name='h3_visualization'):
    """
    The visualization functions are what is used to create each individual
    image.
    The function should be repeatable if not generalizable
    The function will call either the boxplot or density plot functions you
    wrote above

    :param target_var:
    :param input_vars:
    :param output_image_name: the desired name for the image saved
    :return: outputs a saved png file and returns a fig object for testing
    """
    fig = overlapping_density(package='sns', input_vars=input_vars,
                              target_vars=target_vars)

    # Starter code for labeling the image
    plt.xlabel('Annual Payout', figure=fig)
    plt.ylabel('Relative Frequency', figure=fig)
    plt.title('Annual Payout by Veteran Status of Business Owner',
              figure=fig)
    plt.legend()

    # exporting the image to the img folder
    plt.savefig(f'img/{output_image_name}.png', transparent=True, figure=fig)
    return fig


def visualization_four4(
        target_vars=None,
        input_vars=None,
        output_image_name='h4_visualization'):
    """
    The visualization functions are what is used to create each individual
    image.
    The function should be repeatable if not generalizable
    The function will call either the boxplot or density plot functions you
    wrote above

    :param target_var:
    :param input_vars:
    :param output_image_name: the desired name for the image saved
    :return: outputs a saved png file and returns a fig object for testing
    """

    fig = overlapping_density(package='sns', input_vars=input_vars,
                              target_vars=target_vars)

    # Starter code for labeling the image
    plt.xlabel('Number of Employees Hired', figure=fig)
    plt.ylabel('Relative Frequency', figure=fig)
    plt.title('Number of Employees Hired by Veteran Status of Business Owner',
              figure=fig)
    plt.legend()

    # exporting the image to the img folder
    plt.savefig(f'img/{output_image_name}.png', transparent=True, figure=fig)
    return fig


def visualization_five5(
        target_vars=None,
        input_vars=None,
        output_image_name='h5_visualization'):
    """
    The visualization functions are what is used to create each individual
    image.
    The function should be repeatable if not generalizable
    The function will call either the boxplot or density plot functions you
    wrote above

    :param target_var:
    :param input_vars:
    :param output_image_name: the desired name for the image saved
    :return: outputs a saved png file and returns a fig object for testing
    """
    fig = overlapping_density(package='sns', input_vars=input_vars,
                              target_vars=target_vars)

    # Starter code for labeling the image
    plt.xlabel('Annual Payout', figure=fig)
    plt.ylabel('Relative Frequency', figure=fig)
    plt.title('Annual Payout by Ethnicity of Business Owner',
              figure=fig)
    plt.legend()

    # exporting the image to the img folder
    plt.savefig(f'img/{output_image_name}.png', transparent=True, figure=fig)
    return fig
