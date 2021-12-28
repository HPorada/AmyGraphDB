<?xml version='1.0' encoding='utf-8'?>
<graphml xmlns="http://graphml.graphdrawing.org/xmlns" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd">
  <key id="d7" for="edge" attr.name="weight" attr.type="long" />
  <key id="d6" for="node" attr.name="pH" attr.type="string" />
  <key id="d5" for="node" attr.name="temperature" attr.type="string" />
  <key id="d4" for="node" attr.name="lifestyle" attr.type="string" />
  <key id="d3" for="node" attr.name="title" attr.type="string" />
  <key id="d2" for="node" attr.name="size" attr.type="long" />
  <key id="d1" for="node" attr.name="group" attr.type="long" />
  <key id="d0" for="node" attr.name="label" attr.type="string" />
  <graph edgedefault="directed">
    <node id="amyloids/BASS3">
      <data key="d0">BASS3</data>
      <data key="d1">4</data>
      <data key="d2">10</data>
    </node>
    <node id="sequences/PPT_1">
      <data key="d3">&lt;a href="javascript:alert(VDLRDAKGVQVGDGNVQINRF)"&gt;VDLRDAKGVQVGDGNVQINRF&lt;/a&gt;</data>
      <data key="d0">ORT49035.1_103_123</data>
      <data key="d1">3</data>
      <data key="d2">10</data>
    </node>
    <node id="sequences/PPT_8">
      <data key="d3">&lt;a href="javascript:alert(VNAPDARGLQVGTGNTQINNF)"&gt;VNAPDARGLQVGTGNTQINNF&lt;/a&gt;</data>
      <data key="d0">ORT49016.1_1_21</data>
      <data key="d1">3</data>
      <data key="d2">10</data>
    </node>
    <node id="sequences/PPT_8_Met">
      <data key="d3">&lt;a href="javascript:alert(MNAPDARGLQVGTGNTQINNF)"&gt;MNAPDARGLQVGTGNTQINNF&lt;/a&gt;</data>
      <data key="d0">nan</data>
      <data key="d1">3</data>
      <data key="d2">10</data>
    </node>
    <node id="organisms/Frankia_sp_KB5">
      <data key="d4">symbiont roslin</data>
      <data key="d5">ok. 25</data>
      <data key="d6">nan</data>
      <data key="d0">Frankia_sp_KB5</data>
      <data key="d1">5</data>
      <data key="d2">10</data>
    </node>
    <edge source="amyloids/BASS3" target="sequences/PPT_1">
      <data key="d7">1</data>
    </edge>
    <edge source="amyloids/BASS3" target="sequences/PPT_8">
      <data key="d7">1</data>
    </edge>
    <edge source="amyloids/BASS3" target="sequences/PPT_8_Met">
      <data key="d7">1</data>
    </edge>
    <edge source="sequences/PPT_1" target="sequences/PPT_1">
      <data key="d7">1</data>
    </edge>
    <edge source="sequences/PPT_8" target="sequences/PPT_8">
      <data key="d7">1</data>
    </edge>
    <edge source="sequences/PPT_8_Met" target="sequences/PPT_8_Met">
      <data key="d7">1</data>
    </edge>
    <edge source="organisms/Frankia_sp_KB5" target="amyloids/BASS3">
      <data key="d7">1</data>
    </edge>
  </graph>
</graphml>
