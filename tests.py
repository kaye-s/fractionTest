from fraction import Fraction
import unittest

class TestInit(unittest.TestCase):
  #several of these will need to check to see if an exception is raised
  def test_divZero(self):
    with self.assertRaises(ZeroDivisionError,msg="Denominator of zero fails to raise DivByZero"):
      a = Fraction(1,0)

  def test_divZeroSafe(self):
    #Will the fraction 0/0 be accepted
    a = Fraction(0,0)
    self.assertEqual(a.numerator, 0, "Numerator should be 0")
    self.assertEqual(a.denominator, 0, "Zero denominator SAFE because numerator is 0")

  def test_default(self):
    #will the 0 argument version of the constructor produce the correct fraction?
    a = Fraction()
    self.assertEqual(a.numerator, 0, "Numerator does not equal default value")
    self.assertEqual(a.denominator, 1, "Denominator does not equal default value")

  def test_oneArg(self):
    #will the 1 argument version of the constructor produce the correct fraction?
    a = Fraction(2)
    self.assertEqual(a.numerator, 2, "Numerator is not updated")
    self.assertEqual(a.denominator, 1, "Denominator does not equal default value")

  def test_twoArg(self):
    #will the 2 argument version of the constructor produce the correct fraction?
    a = Fraction(2, 3)
    self.assertEqual(a.numerator, 2, "Numerator is not updated")
    self.assertEqual(a.denominator, 3, "Denominator is not updated")

  def test_invalidArg(self):
    #will constructor through an exception if non-numeric data is passed?
    with self.assertRaises(TypeError,msg="Non-numeric input fails to raise TypeError"):
      a = Fraction("One")

  def test_reduced(self):
    #if the inputs share a factor, is the fraction reduced? i.e. 2/4 = 1/2
    a = Fraction(2, 4)
    self.assertEqual(a.numerator, 1, "Numerator is not reduced")
    self.assertEqual(a.denominator, 2, "Denominator is not reduced")

########################################################################################
  def test_negative(self):
    #if both inputs are negative, cancel out and display positive value
    a = Fraction(-1, -2)
    self.assertEqual(a.numerator, 1, "Numerator and Denominator should cancel out")
    self.assertEqual(a.denominator, 2, "Numerator and Denominator should cancel out")
########################################################################################

  def test_decimal(self):
    #if the input is a decimal, will it raise a type error?
    with self.assertRaises(TypeError,msg="Decimal input fails to raise TypeError"):
      a = Fraction(2.4)

class TestStr(unittest.TestCase):
  def test_displayfraction(self):
    a = Fraction(1,2)
    self.assertEqual(" 1/2 ",a.__str__())

  def test_displayInt(self):
    #if the denominator is 1, does display omit the /1?
    a = Fraction(2, 1)
    self.assertEqual(" 2 ", a.__str__(), "String should omit the /1 when the denominator is 1")

  def test_displayNeg(self):
    #if the fraction is negative, is it possible to erroneously have it display 1/-2, vs -1/2?
    a = Fraction(1, -2)
    self.assertEqual(" -1/2 ", a.__str__(), "Negative signs should display first")

########################################################################################
  def test_displayCompound(self):
    #if the numerator is larger than the denominator, will it display as a compound fraction?
    a = Fraction(4,3)
    self.assertEqual(" 1 and 1/3 " , a.__str__())
########################################################################################

class TestFloat(unittest.TestCase):
  def test_zeroNumerator(self):
    #if the numerator is a 0, will it return 0?
    a = Fraction(0,1)
    self.assertEqual(0, a.__float__(), "Zero numerator should produce 0")

  def test_oneDenominator(self):
    #If the denominator is 1, will it return the same as numerator?
    a = Fraction(2,1)
    self.assertEqual(2, a.__float__(), "One denominator should produce num")

  def test_sameNum(self):
    #if the numerator and denominator are equal, will the result be 1?
    a = Fraction(2,2)
    self.assertEqual(1, a.__float__(), "Same numerator and denominator, result should be 1")

  def test_finiteDecimal(self):
    #if the result is finite, does it produce the correct decimal?
    a = Fraction(3,4)
    self.assertEqual(0.75, a.__float__(), "Finite result, should produce accurate decimal")

  def test_infiniteDecimal(self):
    #if the result is infinite, does it compute and round the decimal to 3 decimal places?
    a = Fraction(2,3)
    self.assertEqual(0.667, a.__float__(), "Infinite result, should produce accurate decimal (rounded to 3 places)")

class TestAdd(unittest.TestCase):
  def setUp(self):
    self.Fraction = Fraction(1,3)

  def test_none(self):
    #if add does not have an input, will it raise a type error?
    with self.assertRaises(TypeError,msg="Add must have one argument"):
      self.Fraction.__add__(None)

  def test_num(self):
    #if the input of add is not a fraction, will it raise a type error?
    with self.assertRaises(TypeError,msg="Argument of add must be a fraction"):
      self.Fraction.__add__(2)

  def test_sameDenominator(self):
    #Trying simple addition two fractions with the same denominator
    a = Fraction(1,3)
    self.assertEqual(Fraction(2,3), self.Fraction.__add__(a), "Same denominator, Did not produce the correct fraction")

  def test_sameDenominatorReduction(self):
    #If two fractions have the same denominator but produce a whole, will it reduce
    a = Fraction(2,3)
    self.assertEqual(Fraction(1,1), self.Fraction.__add__(a), "When adding up to a whole, the result should be the Fraction 1/1")

  def test_wholeNum(self):
    #Can it add a whole number fraction to a fraction? (Different denominators and simple)
    a = Fraction(3,1)
    self.assertEqual(Fraction(10,3), self.Fraction.__add__(a), "Error when adding a whole number to a fraction")

  def test_differentDenominator(self):
    # What if the denominators are completely different? (complex addition)
    a = Fraction(3,4)
    self.assertEqual(Fraction(13,12), self.Fraction.__add__(a), "Different denominators, did not produce the correct fraction")

  def test_reduction(self):
    # Must always produce result as most reduced
    a = Fraction(1,6)
    self.assertEqual(Fraction(1,2), self.Fraction.__add__(a), "After addition, result must be reduced")


class TestSub(unittest.TestCase):
  def setUp(self):
    self.Fraction = Fraction(2, 3)

  def test_none(self):
    # if sub does not have an input, will it raise a type error?
    with self.assertRaises(TypeError, msg="Sub must have one argument"):
      self.Fraction.__sub__(None)

  def test_num(self):
    # if the input of sub is not a fraction, will it raise a type error?
    with self.assertRaises(TypeError, msg="Argument of sub must be a fraction"):
      self.Fraction.__sub__(2)

  def test_sameDenominator(self):
    # Trying simple subtraction two fractions with the same denominator
    a = Fraction(1, 3)
    self.assertEqual(Fraction(1, 3), self.Fraction.__sub__(a), "Same denominator, Did not produce the correct fraction")

  def test_sameDenominatorZero(self):
    # If two fractions have the same denominator and are equal, will it produce the fraction 0/0
    a = Fraction(2, 3)
    self.assertEqual(Fraction(0, 0), self.Fraction.__sub__(a), "When adding up to a whole, the result should be the Fraction 1/1")

  def test_neg(self):
    # When subtracting into the negative, does the resulting fraction have the negative sign first
    a = Fraction(7, 3)
    self.assertEqual(Fraction(-5, 3), self.Fraction.__sub__(a), "Negative result should have negation in the numerator")

  def test_wholeNum(self):
    # Can it subtract a whole number fraction from a fraction? (Different denominators negative result)
    a = Fraction(3, 1)
    self.assertEqual(Fraction(-7, 3), self.Fraction.__sub__(a), "Error when subtracting a whole number from a fraction")

  def test_differentDenominator(self):
    # What if the denominators are completely different? (complex subtraction)
    a = Fraction(1, 4)
    self.assertEqual(Fraction(5, 12), self.Fraction.__sub__(a),
                     "Different denominators, did not produce the correct fraction")

  def test_reduction(self):
    # Must always produce result as most reduced
    a = Fraction(1, 6)
    self.assertEqual(Fraction(1, 2), self.Fraction.__sub__(a), "After subtraction, result must be reduced")

class TestMul(unittest.TestCase):
  def setUp(self):
    self.Fraction = Fraction(1, 3)

  def test_none(self):
    # if mul does not have an input, will it raise a type error?
    with self.assertRaises(TypeError, msg="Mul must have one argument"):
      self.Fraction.__mul__(None)

  def test_num(self):
    # if the input of mul is not a fraction, will it raise a type error?
    with self.assertRaises(TypeError, msg="Argument of mul must be a fraction"):
      self.Fraction.__mul__(2)

  def test_sameDenominator(self):
    # Trying simple multiplication two fractions with the same denominator
    a = Fraction(1, 2)
    self.assertEqual(Fraction(1, 6), self.Fraction.__mul__(a), "Same denominator, Did not produce the correct fraction")

  def test_differentDenominator(self):
    # What if the denominators are completely different?
    a = Fraction(1, 4)
    self.assertEqual(Fraction(1, 12), self.Fraction.__mul__(a),
                     "Different denominators, did not produce the correct fraction")

  def test_reduction(self):
    # Must always produce result as most reduced
    a = Fraction(2, 4)
    self.assertEqual(Fraction(1, 6), self.Fraction.__mul__(a), "After multiplication, result must be reduced")

  def test_wholeNumSimple(self):
    # Can it multiply a whole number fraction and a fraction? (Different denominators reduced)
    a = Fraction(2, 1)
    self.assertEqual(Fraction(2, 3), self.Fraction.__mul__(a), "Error when multiplying a whole number from a fraction (simple)")

  def test_wholeNumComplex(self):
    # Can it multiply a whole number fraction and a fraction? (Different denominators reduced to 1
    a = Fraction(3, 1)
    self.assertEqual(Fraction(1, 1), self.Fraction.__mul__(a), "Error when multiplying a whole number from a fraction (complex)")

class TestTrueDiv(unittest.TestCase):
  def setUp(self):
    self.Fraction = Fraction(1, 3)

  def test_none(self):
    # if div does not have an input, will it raise a type error?
    with self.assertRaises(TypeError, msg="trueDiv must have one argument"):
      self.Fraction.__truediv__(None)

  def test_num(self):
    # if the input of div is not a fraction, will it raise a type error?
    with self.assertRaises(TypeError, msg="Argument of trueDiv must be a fraction"):
      self.Fraction.__truediv__(2)

  def test_sameFraction(self):
    # if the two fractions are the same, is the result 1?
    a = Fraction(1, 3)
    self.assertEqual(Fraction(1, 1), self.Fraction.__truediv__(a), "Same fraction, Did not produce the 1")

  def test_reductionSameDenominator(self):
    # Must always produce result as most reduced, same denominator division
    a = Fraction(2, 3)
    self.assertEqual(Fraction(1, 2), self.Fraction.__truediv__(a), "After division, result must be reduced")

  def test_differentDenominator(self):
    # What if the denominators are completely different?
    a = Fraction(1, 4)
    self.assertEqual(Fraction(4, 3), self.Fraction.__truediv__(a),
                     "Different denominators, did not produce the correct fraction")

  def test_reductionDifferentDenominator(self):
    # Trying division two fractions with different denominators, must reduce
    a = Fraction(1, 6)
    self.assertEqual(Fraction(2, 1), self.Fraction.__truediv__(a), "Different denominator, Result must reduce")

  def test_wholeNum(self):
    # Can it multiply a whole number fraction and a fraction? (Different denominators reduced)
    a = Fraction(2, 1)
    self.assertEqual(Fraction(1, 6), self.Fraction.__truediv__(a), "Error when dividing a whole number from a fraction")
