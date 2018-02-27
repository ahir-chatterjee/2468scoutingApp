//
//  GlobalState.swift
//  Scouting Application
//
//  Created by Vrishab Madduri on 11/15/17.
//  Copyright © 2017 Vrishab Madduri. All rights reserved.
//

import Foundation

public class State {
    var hang = "Unknown"
    var match = -1
    var team = -1
    var color = "Unknown"
    var score = -1
    var comment = "Unknown"
    var allianceswitch = 0
    var opposingswitch = 0
    var assistance = "Unknown"
    var vault = 0
    var penalty = "Unknown"
    var line = "Unknown"
    var autoswitch = 0
    var autoscale = 0
    var timerValues = [Int]()
    var failed = 0
    var failureArray: [Bool] = []
    var pickerView = "left"
    var assistView = -1
    var randomSwitch = "Unknown"
    var randomScale = "Unknown"
    
    static var global = State()
}

