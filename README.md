## Overview

**Odoo Preventive Maintenance** 
is a custom Odoo module that enhances the default Maintenance application by introducing a flexible preventive maintenance planning system based on equipment usage rather than relying only on dates.

The module allows organizations to define maintenance plans for equipment based on operational intervals such as kilometers, hours, days, weeks, or years. It also integrates spare parts management into maintenance requests, ensuring accurate inventory tracking during repair operations.

This project was implemented as part of an Odoo developer technical task focused on extending the Maintenance application with practical business logic.

---

## Key Features

### Preventive Maintenance Planning

Each equipment can have multiple maintenance plans that trigger maintenance operations when a specific usage threshold is reached.

Example:

| Equipment | Interval  | Task               |
| --------- | --------- | ------------------ |
| Car       | 10,000 km | Change oil         |
| Car       | 20,000 km | Replace air filter |

Maintenance plans define:

* Maintenance task
* Trigger interval
* Unit of measurement

---

### Multiple Maintenance Units

Maintenance scheduling can be based on several measurement units:

* Hours
* Days
* Weeks
* Years
* Kilometers

This allows maintenance to reflect real equipment usage rather than fixed dates.

---

### Spare Parts Management

Maintenance requests include a dedicated **Spare Parts** tab where technicians can:

* Select spare parts used during maintenance
* View available stock
* Enter quantities consumed

The system validates stock availability before confirming consumption.

---

### Spare Parts Validation Wizard

A validation wizard is used to confirm spare parts usage. The wizard:

* Displays selected spare parts
* Shows current stock availability
* Calculates remaining quantity after consumption
* Prevents invalid quantities

---

### Inventory Integration

Spare parts used during maintenance are consumed through Odoo's inventory system to ensure accurate stock tracking.

---

### Automatic Maintenance Scheduling

A scheduled background job periodically checks equipment maintenance plans and automatically creates preventive maintenance requests when conditions are met.

---

## Module Structure

```
odoo-preventive-maintenance
│
├── models
│   ├── maintenance_equipment.py
│   ├── maintenance_request.py
│   ├── maintenance_equipment_plan.py
│   ├── maintenance_request_line.py
│   ├── product_template.py
│   └── mrp_workcenter.py
│
├── views
│
├── wizard
│
├── data
│
├── security
│
├── __init__.py
└── __manifest__.py
```

---

## Main Models

### Maintenance Equipment Plan

Defines maintenance intervals and tasks for each equipment.

Fields include:

* Task description
* Maintenance interval
* Measurement unit
* Completion status

---

### Maintenance Request Line

Stores spare parts consumed during maintenance operations.

Fields include:

* Product
* Quantity
* Available stock
* Remaining stock after consumption

---

### Product Template Extension

Adds a flag to identify products that can be used as spare parts.

---

### Work Center Extension

Adds maintenance configuration fields to manufacturing work centers.

---

## Dependencies

This module depends on the following Odoo modules:

* base
* mail
* maintenance
* hr_maintenance
* mrp
* mrp_maintenance

---

## Technologies Used

* Python
* Odoo ORM
* XML Views
* Odoo Wizards
* Scheduled Actions (Cron Jobs)

---

## Installation

1. Copy the module into the Odoo addons directory.
2. Update the apps list in Odoo.
3. Install the module from the Apps menu.

---

## Usage

1. Create or open equipment in the Maintenance module.
2. Define maintenance plans for the equipment.
3. Set maintenance intervals and tasks.
4. When maintenance is performed, record spare parts used.
5. Validate spare parts consumption through the wizard.

---

## Author

Seif Hany

Odoo Developer

---

## License

LGPL-3
