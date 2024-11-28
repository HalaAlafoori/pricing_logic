# Pricing Logic - ERPNext App

## Overview

The **Pricing Logic** app is a modular add-on designed to extend ERPNext's pricing functionality by replacing the legacy pricing rules with a more flexible, extendable solution. Initially, the app will support **Tiered Pricing** and **Cumulative Tiered Pricing**, with plans to easily add more pricing logic types in the future (e.g., volume discounts, promotions). This app allows for dynamic, real-time price updates in sales transactions and is fully configurable through a simple, modular design.

## Features

- **Tiered Pricing**: Set price tiers based on quantity ranges.
- **Cumulative Tiered Pricing**: Apply cumulative pricing logic across tiers, where each tier’s price multiplies with the quantity in that tier and adds to the next.
- **Modular Architecture**: Easily extendable to add new pricing rules like volume discounts, "Buy X Get Y" promotions, and more.
- **Real-time Price Updates**: Use JavaScript to dynamically update pricing in sales transactions based on the selected pricing rule.
- **Customizable Forms and Views**: Manage pricing rules and tier structures through ERPNext's intuitive interface.

## Installation

Follow the steps below to install and configure the **Pricing Logic** app on your ERPNext instance:

### 1. Prerequisites

- **ERPNext**: Ensure you have ERPNext set up and running.
- **Frappe**: This app relies on Frappe, the underlying framework of ERPNext.

### 2. Clone the Repository

```bash
git clone https://github.com/yourusername/pricing_logic.git
