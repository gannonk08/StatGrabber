# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import psycopg2
import logging
from stat_grabber.items import awayTeamItem
from stat_grabber.items import homeTeamItem
from stat_grabber.items import requestURLItem
from scrapy.conf import settings
from scrapy.exceptions import DropItem


class StatGrabberPipeline(object):
  def __init__(self):
    self.connection = psycopg2.connect(host='localhost', database='stat_grabber', user='Gannon')
    self.cursor = self.connection.cursor()

  def process_item(self, item, spider):
    try:
      if type(item) is awayTeamItem:
        nfl = """nfl_scores"""
        self.cursor.execute("""INSERT INTO """ + nfl + """ (game_id, team, q1, q2, q3, q4, final) VALUES(%s, %s, %s, %s, %s, %s, %s)""", (item.get('gameId'), item.get('awayTeam'), item.get('Q1'), item.get('Q2'), item.get('Q3'), item.get('Q4'), item.get('final')))
      elif type(item) is homeTeamItem:
        nfl = """nfl_scores"""
        self.cursor.execute("""INSERT INTO """ + nfl + """ (game_id, team, q1, q2, q3, q4, final) VALUES(%s, %s, %s, %s, %s, %s, %s)""", (item.get('gameId'), item.get('homeTeam'), item.get('Q1'), item.get('Q2'), item.get('Q3'), item.get('Q4'), item.get('final')))
      self.connection.commit()
      self.cursor.fetchall()

    except psycopg2.DatabaseError, e:
      print "Error: %s" % e
    return item
