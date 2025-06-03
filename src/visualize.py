import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import math
import warnings
pd.options.mode.chained_assignment = None
warnings.filterwarnings('ignore')


def plotCorrelationHeatmap(df):
    fig, ax = plt.subplots(figsize=(20, 5), dpi=80)
    df = df.loc[:, df.nunique() > 1]
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='crest', vmin=-1, vmax=1, ax=ax )
    ax.set_title('\nCorrelation of All Numeric Columns in Dataset\n', fontsize=22, color='grey', loc='center', fontname='DejaVu Sans', weight='bold')
    ax.patch.set_edgecolor('black')
    ax.patch.set_linewidth(1.5)
    plt.tight_layout()
    plt.show()

def plotFrequencyGridSmart(df, cols=None, nCols=6, figHeightPerRow=4, figWidthPerPlot=2.5, title=None, maxStrLen=20, maxUniqueFrac=0.5):
    if cols is None:
        cols = df.columns.tolist()

    usableCols = []
    for col in cols:
        if df[col].dtype == 'O' or pd.api.types.is_string_dtype(df[col]):
            avg_len = df[col].dropna().astype(str).str.len().mean()
            unique_frac = df[col].nunique(dropna=True) / len(df)
            if avg_len < maxStrLen and unique_frac < maxUniqueFrac:
                usableCols.append(col)
        else:
            usableCols.append(col)

    nVars = len(usableCols)
    if nVars == 0:
        print("No suitable columns to plot.")
        return

    nRows = math.ceil(nVars / nCols)
    figWidth = figWidthPerPlot * nCols
    figHeight = figHeightPerRow * nRows

    palette = sns.color_palette("Pastel1", n_colors=nVars)

    fig, axes = plt.subplots(nRows, nCols, figsize=(figWidth, figHeight), squeeze=False)
    axes = axes.flatten()

    for i, col in enumerate(usableCols):
        ax = axes[i]
        if pd.api.types.is_numeric_dtype(df[col]):
            sns.histplot(data=df, x=col, ax=ax, color=palette[i % len(palette)], bins=30, kde=False)
        else:
            sns.countplot(data=df, x=col, ax=ax, color=palette[i % len(palette)])
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

        ax.set_title(col, fontsize=12)
        ax.set_xlabel("")
        ax.set_ylabel("")
        ax.grid(color='#b2d6c7', linewidth=1, axis='y', alpha=.3)
        ax.set_facecolor((1, 1, 1, 0.9))
        ax.patch.set_edgecolor('black')

    for j in range(nVars, nRows * nCols):
        fig.delaxes(axes[j])

    if title:
        plt.suptitle(title, fontsize=18, color='grey', fontweight='bold', y=1.02)

    plt.tight_layout(rect=[0, 0, 1, 0.98])
    plt.show()

def plotBoxplotGrid(df, nCols=8, figHeightPerRow=4, figWidthPerPlot=2.5, title=None):
    cols = df.select_dtypes(include="number").columns.tolist()
    if cols is None:
        cols = [col for col in df.select_dtypes(include=[np.number]).columns]
    nVars = len(cols)
    nRows = math.ceil(nVars / nCols)
    figWidth = figWidthPerPlot * nCols
    figHeight = figHeightPerRow * nRows

    palette = sns.color_palette("Pastel1", n_colors=nVars)

    fig, axes = plt.subplots(nRows, nCols, figsize=(figWidth, figHeight), squeeze=False)
    axes = axes.flatten()
    for i, col in enumerate(cols):
        sns.boxplot(y=df[col], ax=axes[i], color=palette[i % len(palette)], width=0.6, fliersize=2)
        axes[i].set_title(col, fontsize=12)
        axes[i].set_ylabel("")
        #axes[i].set_yticklabels([])
        axes[i].set_xticks([])
        axes[i].grid(color='#b2d6c7', linewidth=1, axis='y', alpha=.3)
        axes[i].set_facecolor((1, 1, 1, 0.9))
        axes[i].patch.set_edgecolor('black')
    
    for j in range(nVars, nRows * nCols):
        fig.delaxes(axes[j])
    if title:
        plt.suptitle(title, fontsize=18, color='grey', fontweight='bold', y=1.02)
    plt.tight_layout(rect=[0, 0, 1, 0.98])
    plt.show()