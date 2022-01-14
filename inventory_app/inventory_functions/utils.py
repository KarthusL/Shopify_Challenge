import random
from random import randrange

from flask import flash
from sqlalchemy import func

from inventory_app import db
from inventory_app.models.models import Inventory


def create_sample_data():
    row = 0
    try:
        row = db.session.query(func.max(Inventory.id)).first()
    except:
        flash('There was a problem when creating sample data')
    if row is not None:
        index = row[0] if row[0] is not None else 0
    else:
        index = 0
    while True:
        index += 1
        item = Inventory(index, random.choice(item_list), random.choice(planet_list), randrange(100000))
        db.session.add(item)

        if index % 5 == 0:
            break
    db.session.commit()


planet_list = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

item_list = ['Iron ore',
             'Copper ore',
             'Silicon ore',
             'Titanium ore',
             'Stone',
             'Coal',
             'Log',
             'Plant fuel',
             'Fire ice',
             'Kimberlite ore',
             'Fractal silicon',
             'Optical grating crystal',
             'Spiniform stalagmite crystal',
             'Unipolar magnet',
             'Iron ingot',
             'Copper ingot',
             'High-purity silicon',
             'Titanium ingot',
             'Stone brick',
             'Energetic graphite',
             'Steel',
             'Titanium alloy',
             'Glass',
             'Titanium glass',
             'Prism',
             'Diamond',
             'Crystal silicon',
             'Gear',
             'Magnet',
             'Magnetic coil',
             'Electric motor',
             'Electromagnetic turbine',
             'Super-magnetic ring',
             'Particle container',
             'Strange matter',
             'Circuit board',
             'Processor',
             'Quantum chip',
             'Microcrystalline component',
             'Plane filter',
             'Particle broadband',
             'Plasma exciter',
             'Photon combiner',
             'Solar sail',
             'Water',
             'Crude oil',
             'Refined oil',
             'Sulfuric acid',
             'Hydrogen',
             'Deuterium',
             'Antimatter',
             'Critical photon',
             'Hydrogen fuel rod',
             'Deuteron fuel rod',
             'Antimatter fuel rod',
             'Plastic',
             'Graphene',
             'Carbon nanotube',
             'Organic crystal',
             'Titanium crystal',
             'Casimir crystal',
             'Graviton lens',
             'Space warper',
             'Annihilation constraint sphere',
             'Thruster',
             'Reinforced thruster',
             'Logistics drone',
             'Logistics vessel',
             'Frame material',
             'Dyson sphere component',
             'Small carrier rocket',
             'Foundation',
             'Accelerant Mk.I',
             'Accelerant Mk.II',
             'Accelerant Mk.III',
             'Conveyor belt MK.I',
             'Conveyor belt MK.II',
             'Conveyor belt MK.III',
             'Sorter MK.I',
             'Sorter MK.II',
             'Sorter MK.III',
             'Splitter(4-direction)',
             'Storage MK.I',
             'Storage MK.II',
             'Storage tank',
             'Assembling machine Mk.I',
             'Assembling machine Mk.II',
             'Assembling machine Mk.III',
             'Plane smelter',
             'Tesla tower',
             'Wireless power tower',
             'Satellite substation',
             'Wind turbine',
             'Thermal power station',
             'Mini fusion power station',
             'Mining machine',
             'Smelter',
             'Oil extractor',
             'Oil refinery',
             'Water pump',
             'Chemical plant',
             'Fractionator',
             'Spray coater',
             'Solar panel',
             'Accumulator',
             'Accumulator(full)',
             'EM-Rail Ejector',
             'Ray receiver',
             'Vertical launching silo',
             'Energy exchanger',
             'Miniature particle collider',
             'Artificial star',
             'Planetary Logistics Station',
             'Interstellar Logistics Station',
             'Orbital Collector',
             'Matrix lab',
             'Electromagnetic matrix',
             'Energy matrix',
             'Structure matrx']
