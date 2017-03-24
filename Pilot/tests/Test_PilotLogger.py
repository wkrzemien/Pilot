""" Unit tests for PilotLogger
"""

#pylint: disable=protected-access, missing-docstring, invalid-name, line-too-long

import unittest
import os
from Pilot.PilotLogger import PilotLogger, getPilotUUIDFromFile
from Pilot.PilotLoggerTools import getUniqueIDAndSaveToFile

class TestPilotLogger( unittest.TestCase ):

  def setUp( self ):
    self.testFile = 'UUID_to_store'
    self.testCfgFile = 'TestPilotLogger.cfg'
    getUniqueIDAndSaveToFile( self.testFile )
    self.logger = PilotLogger(self.testCfgFile)
    self.badFile = '////'
    self.nonExistentFile = 'abrakadabraToCzaryIMagia'
  def tearDown( self ):
    try:
      os.remove( self.testFile )
    except OSError:
      pass


class TestGetPilotUUIDFromFile( TestPilotLogger ):

  def test_success( self ):
    uuid = getPilotUUIDFromFile( self.testFile )
    self.assertTrue( uuid )

  def test_failureBadFile( self ):
    uuid = getPilotUUIDFromFile( self.badFile )
    self.assertFalse( uuid )

  def test_failureNonExistent( self ):
    uuid = getPilotUUIDFromFile( self.nonExistentFile )
    self.assertFalse( uuid )

class TestPilotLogger_isCorrectStatus( TestPilotLogger ):

  def test_success( self ):
    for status in self.logger.STATUSES:
      self.assertTrue( self.logger._isCorrectStatus( status ) )

  def test_failure( self ):
    self.assertFalse( self.logger._isCorrectStatus( 'mamma Mia' ) )

  def test_failureEmpty( self ):
    self.assertFalse( self.logger._isCorrectStatus( '' ) )

class TestPilotLogger_connect( TestPilotLogger ):
  pass
class TestPilotLogger_sendMessage( TestPilotLogger ):

  # here some mocks needed
  def test_success( self ):
    pass
  def test_failure( self ):
    pass

class TestPilotLoggersendMessage( TestPilotLogger ):

  # here some mocks needed
  def test_success( self ):
    pass

  def test_NotCorrectFlag( self ):
    self.assertFalse( self.logger.sendMessage( '', 'badFlag' ) )

if __name__ == '__main__':
  suite = unittest.defaultTestLoader.loadTestsFromTestCase( TestPilotLogger )
  suite.addTest( unittest.defaultTestLoader.loadTestsFromTestCase( TestGetPilotUUIDFromFile ) )
  suite.addTest( unittest.defaultTestLoader.loadTestsFromTestCase( TestPilotLogger_connect ) )
  suite.addTest( unittest.defaultTestLoader.loadTestsFromTestCase( TestPilotLogger_isCorrectStatus ) )
  suite.addTest( unittest.defaultTestLoader.loadTestsFromTestCase( TestPilotLogger_sendMessage ) )
  suite.addTest( unittest.defaultTestLoader.loadTestsFromTestCase( TestPilotLoggersendMessage ) )
  testResult = unittest.TextTestRunner( verbosity = 2 ).run( suite )
