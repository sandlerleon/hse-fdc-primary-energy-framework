# -*- coding: utf-8 -*-
"""
Regenerates Figures 1-4 for the HSE-FDC manuscript, per Discover
Sustainability's figure formatting requirements: no title baked into the
artwork (titles/captions live in the manuscript text only), sans-serif
(Arial/Helvetica) lettering at 8-12 pt.
"""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import hsefdc_model as m

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'DejaVu Sans']
plt.rcParams['font.size'] = 10
plt.rcParams['axes.titlesize'] = 0  # titles are not used in-figure
plt.rcParams['axes.labelsize'] = 11
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['legend.fontsize'] = 9

OUTDIR = os.path.dirname(os.path.abspath(__file__))


def fig1_gas_vs_wave():
    fig, ax = plt.subplots(figsize=(6.5, 4.235))
    labels = ['Simple-cycle\n(established offshore practice)', 'Combined-cycle\n(Appomattox-precedented)']
    gt = [m.simple_cycle_rated_mw, m.combined_cycle_rated_mw]
    wave = [m.wec_avg_mw, m.wec_avg_mw]
    shares = [m.wave_share_simple, m.wave_share_combined]

    x = range(len(labels))
    ax.bar(x, gt, color='#123a5e', label='Gas turbine (rated)')
    ax.bar(x, wave, bottom=gt, color='#3f8fb5', label='Wave array (avg., 25% capacity factor)')
    for i, (g, w, s) in enumerate(zip(gt, wave, shares)):
        ax.annotate(f'wave: {w:.2f} MW\n({s:.1f}% of supply)', xy=(i, g + w),
                    xytext=(i, g + w + 8), ha='center', fontsize=9, color='#444444')
    ax.set_xticks(list(x))
    ax.set_xticklabels(labels)
    ax.set_ylabel('Average power supply (MW)')
    ax.legend(loc='upper left', frameon=True)
    ax.set_ylim(0, max(gt) * 1.35)
    fig.tight_layout()
    fig.savefig(os.path.join(OUTDIR, 'fig1_gas_vs_wave_supply.png'), dpi=300)
    plt.close(fig)


def fig2_pue_benchmarks():
    fig, ax = plt.subplots(figsize=(6.6, 4.0))
    labels = ['Conventional\nland DC\n(air/liquid-cooled)', 'Modern\nhyperscale\n(best practice)',
              'Microsoft\nNatick\n(real, renewable-tied)', 'HSE-FDC\n(modeled,\nthis study)']
    values = [m.PUE_CONVENTIONAL_LAND_DC, m.PUE_MODERN_BEST_PRACTICE, m.PUE_NATICK_REAL, m.facility_pue]
    colors = ['#4a5568', '#8fa8bf', '#4c8c5a', '#1f6f8b']
    bars = ax.bar(labels, values, color=colors)
    for b, v in zip(bars, values):
        ax.annotate(f'{v:.2f}', xy=(b.get_x() + b.get_width() / 2, v), xytext=(0, 4),
                    textcoords='offset points', ha='center', fontsize=10)
    ax.set_ylabel('PUE')
    ax.set_ylim(0.95, 1.5)
    ax.axhline(1.0, color='#888888', linewidth=0.8)
    fig.tight_layout()
    fig.savefig(os.path.join(OUTDIR, 'fig2_pue_benchmarks.png'), dpi=300)
    plt.close(fig)


def fig3_primary_energy_efficiency():
    fig, ax = plt.subplots(figsize=(6.5, 4.111))
    labels = ['HSE-FDC\nsimple-cycle\n+ CCS', 'HSE-FDC\ncombined-cycle\n+ CCS',
              'Grid-tied DC\n(mixed-fuel\ngrid avg.)', 'Natick-style\n(renewable-\ngrid-tied)']
    values = [
        m.eta_primary_simple * 100, m.eta_primary_combined * 100,
        m.eta_grid_tied * 100, m.eta_renewable_tied * 100,
    ]
    colors = ['#b5651d', '#d9a441', '#8fa8bf', '#4c8c5a']
    bars = ax.bar(labels, values, color=colors)
    for b, v in zip(bars, values):
        ax.annotate(f'{v:.1f}%', xy=(b.get_x() + b.get_width() / 2, v), xytext=(0, 4),
                    textcoords='offset points', ha='center', fontsize=10)
    ax.set_ylabel('Primary energy efficiency (%)\n(fuel/generation energy reaching useful compute)')
    ax.set_ylim(0, 105)
    fig.tight_layout()
    fig.savefig(os.path.join(OUTDIR, 'fig3_primary_energy_efficiency.png'), dpi=300)
    plt.close(fig)


def fig4_carbon_intensity():
    fig, ax = plt.subplots(figsize=(6.5, 4.111))
    labels = ['HSE-FDC\nsimple-cycle\n(no CCS)', 'HSE-FDC\nsimple-cycle\n(+CCS, 90%\ncapture)',
              'HSE-FDC\ncombined-cycle\n(+CCS, 90%\ncapture)', 'US grid\naverage', 'Natick-style\n(renewable-\ngrid-tied)']
    values = [
        m.carbon_simple_no_ccs, m.carbon_simple_ccs, m.carbon_combined_ccs,
        m.US_GRID_AVERAGE_KG_CO2_PER_KWH, m.NATICK_STYLE_KG_CO2_PER_KWH,
    ]
    colors = ['#8c2f2f', '#c17817', '#d9a441', '#8fa8bf', '#4c8c5a']
    bars = ax.bar(labels, values, color=colors)
    for b, v in zip(bars, values):
        ax.annotate(f'{v:.2f}', xy=(b.get_x() + b.get_width() / 2, v), xytext=(0, 4),
                    textcoords='offset points', ha='center', fontsize=10)
    ax.set_ylabel('kg CO$_2$ / kWh delivered to IT load')
    ax.set_ylim(0, max(values) * 1.2)
    fig.tight_layout()
    fig.savefig(os.path.join(OUTDIR, 'fig4_carbon_intensity.png'), dpi=300)
    plt.close(fig)


if __name__ == '__main__':
    fig1_gas_vs_wave()
    fig2_pue_benchmarks()
    fig3_primary_energy_efficiency()
    fig4_carbon_intensity()
    print('wrote 4 figures to', OUTDIR)
