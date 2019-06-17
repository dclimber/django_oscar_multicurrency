# Generated by Django 2.2.2 on 2019-06-17 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0011_currencyawarevaluecondition'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyAwareAbsoluteDiscountBenefit',
            fields=[
            ],
            options={
                'abstract': False,
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('offer.absolutediscountbenefit',),
        ),
        migrations.CreateModel(
            name='CurrencyAwareFixedPriceBenefit',
            fields=[
            ],
            options={
                'abstract': False,
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('offer.fixedpricebenefit',),
        ),
        migrations.CreateModel(
            name='CurrencyAwareShippingAbsoluteDiscountBenefit',
            fields=[
            ],
            options={
                'abstract': False,
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('offer.shippingabsolutediscountbenefit',),
        ),
        migrations.CreateModel(
            name='CurrencyAwareShippingFixedPriceBenefit',
            fields=[
            ],
            options={
                'abstract': False,
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('offer.shippingfixedpricebenefit',),
        ),
    ]
