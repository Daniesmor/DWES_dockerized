# Generated from Scratch.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,12,58,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,3,0,13,
        8,0,1,1,1,1,1,1,1,1,5,1,19,8,1,10,1,12,1,22,9,1,1,1,1,1,1,1,1,1,
        3,1,28,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,5,3,38,8,3,10,3,12,3,
        41,9,3,1,3,1,3,1,3,1,3,3,3,47,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,
        4,56,8,4,1,4,0,0,5,0,2,4,6,8,0,0,63,0,12,1,0,0,0,2,27,1,0,0,0,4,
        29,1,0,0,0,6,46,1,0,0,0,8,55,1,0,0,0,10,13,3,2,1,0,11,13,3,6,3,0,
        12,10,1,0,0,0,12,11,1,0,0,0,13,1,1,0,0,0,14,15,5,1,0,0,15,20,3,4,
        2,0,16,17,5,2,0,0,17,19,3,4,2,0,18,16,1,0,0,0,19,22,1,0,0,0,20,18,
        1,0,0,0,20,21,1,0,0,0,21,23,1,0,0,0,22,20,1,0,0,0,23,24,5,3,0,0,
        24,28,1,0,0,0,25,26,5,1,0,0,26,28,5,3,0,0,27,14,1,0,0,0,27,25,1,
        0,0,0,28,3,1,0,0,0,29,30,5,10,0,0,30,31,5,4,0,0,31,32,3,8,4,0,32,
        5,1,0,0,0,33,34,5,5,0,0,34,39,3,8,4,0,35,36,5,2,0,0,36,38,3,8,4,
        0,37,35,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,42,
        1,0,0,0,41,39,1,0,0,0,42,43,5,6,0,0,43,47,1,0,0,0,44,45,5,5,0,0,
        45,47,5,6,0,0,46,33,1,0,0,0,46,44,1,0,0,0,47,7,1,0,0,0,48,56,5,10,
        0,0,49,56,5,11,0,0,50,56,3,2,1,0,51,56,3,6,3,0,52,56,5,7,0,0,53,
        56,5,8,0,0,54,56,5,9,0,0,55,48,1,0,0,0,55,49,1,0,0,0,55,50,1,0,0,
        0,55,51,1,0,0,0,55,52,1,0,0,0,55,53,1,0,0,0,55,54,1,0,0,0,56,9,1,
        0,0,0,6,12,20,27,39,46,55
    ]

class ScratchParser ( Parser ):

    grammarFileName = "Scratch.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "','", "'}'", "':'", "'['", "']'", 
                     "'true'", "'false'", "'null'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "STRING", "NUMBER", "WS" ]

    RULE_json = 0
    RULE_object = 1
    RULE_pair = 2
    RULE_array = 3
    RULE_value = 4

    ruleNames =  [ "json", "object", "pair", "array", "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    STRING=10
    NUMBER=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class JsonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def object_(self):
            return self.getTypedRuleContext(ScratchParser.ObjectContext,0)


        def array(self):
            return self.getTypedRuleContext(ScratchParser.ArrayContext,0)


        def getRuleIndex(self):
            return ScratchParser.RULE_json

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJson" ):
                listener.enterJson(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJson" ):
                listener.exitJson(self)




    def json(self):

        localctx = ScratchParser.JsonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_json)
        try:
            self.state = 12
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ScratchParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 10
                self.object_()
                pass
            elif token in [ScratchParser.T__4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 11
                self.array()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ScratchParser.RULE_object

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AnObjectContext(ObjectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ScratchParser.ObjectContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ScratchParser.PairContext)
            else:
                return self.getTypedRuleContext(ScratchParser.PairContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnObject" ):
                listener.enterAnObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnObject" ):
                listener.exitAnObject(self)


    class EmptyObjectContext(ObjectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ScratchParser.ObjectContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyObject" ):
                listener.enterEmptyObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyObject" ):
                listener.exitEmptyObject(self)



    def object_(self):

        localctx = ScratchParser.ObjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_object)
        self._la = 0 # Token type
        try:
            self.state = 27
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = ScratchParser.AnObjectContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 14
                self.match(ScratchParser.T__0)
                self.state = 15
                self.pair()
                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ScratchParser.T__1:
                    self.state = 16
                    self.match(ScratchParser.T__1)
                    self.state = 17
                    self.pair()
                    self.state = 22
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 23
                self.match(ScratchParser.T__2)
                pass

            elif la_ == 2:
                localctx = ScratchParser.EmptyObjectContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.match(ScratchParser.T__0)
                self.state = 26
                self.match(ScratchParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ScratchParser.RULE_pair

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class APairContext(PairContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ScratchParser.PairContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(ScratchParser.STRING, 0)
        def value(self):
            return self.getTypedRuleContext(ScratchParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAPair" ):
                listener.enterAPair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAPair" ):
                listener.exitAPair(self)



    def pair(self):

        localctx = ScratchParser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_pair)
        try:
            localctx = ScratchParser.APairContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(ScratchParser.STRING)
            self.state = 30
            self.match(ScratchParser.T__3)
            self.state = 31
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ScratchParser.RULE_array

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ArrayOfValuesContext(ArrayContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ScratchParser.ArrayContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ScratchParser.ValueContext)
            else:
                return self.getTypedRuleContext(ScratchParser.ValueContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayOfValues" ):
                listener.enterArrayOfValues(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayOfValues" ):
                listener.exitArrayOfValues(self)


    class EmptyArrayContext(ArrayContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ScratchParser.ArrayContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyArray" ):
                listener.enterEmptyArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyArray" ):
                listener.exitEmptyArray(self)



    def array(self):

        localctx = ScratchParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = ScratchParser.ArrayOfValuesContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.match(ScratchParser.T__4)
                self.state = 34
                self.value()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ScratchParser.T__1:
                    self.state = 35
                    self.match(ScratchParser.T__1)
                    self.state = 36
                    self.value()
                    self.state = 41
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 42
                self.match(ScratchParser.T__5)
                pass

            elif la_ == 2:
                localctx = ScratchParser.EmptyArrayContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.match(ScratchParser.T__4)
                self.state = 45
                self.match(ScratchParser.T__5)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ScratchParser.RULE_value

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StringjsonContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ScratchParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(ScratchParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringjson" ):
                listener.enterStringjson(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringjson" ):
                listener.exitStringjson(self)


    class ObjectValueContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ScratchParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def object_(self):
            return self.getTypedRuleContext(ScratchParser.ObjectContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObjectValue" ):
                listener.enterObjectValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObjectValue" ):
                listener.exitObjectValue(self)


    class ArrayValueContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ScratchParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def array(self):
            return self.getTypedRuleContext(ScratchParser.ArrayContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayValue" ):
                listener.enterArrayValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayValue" ):
                listener.exitArrayValue(self)


    class AtomContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ScratchParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(ScratchParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)



    def value(self):

        localctx = ScratchParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_value)
        try:
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ScratchParser.STRING]:
                localctx = ScratchParser.StringjsonContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.match(ScratchParser.STRING)
                pass
            elif token in [ScratchParser.NUMBER]:
                localctx = ScratchParser.AtomContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.match(ScratchParser.NUMBER)
                pass
            elif token in [ScratchParser.T__0]:
                localctx = ScratchParser.ObjectValueContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 50
                self.object_()
                pass
            elif token in [ScratchParser.T__4]:
                localctx = ScratchParser.ArrayValueContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 51
                self.array()
                pass
            elif token in [ScratchParser.T__6]:
                localctx = ScratchParser.AtomContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 52
                self.match(ScratchParser.T__6)
                pass
            elif token in [ScratchParser.T__7]:
                localctx = ScratchParser.AtomContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 53
                self.match(ScratchParser.T__7)
                pass
            elif token in [ScratchParser.T__8]:
                localctx = ScratchParser.AtomContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 54
                self.match(ScratchParser.T__8)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





