//
//  WebInputViewController.swift
//  Scouting Application
//
//  Created by Vrishab Madduri on 11/15/17.
//  Copyright © 2017 Vrishab Madduri. All rights reserved.
//

import Foundation
import UIKit

class WebInputViewController: UIViewController {
    @IBOutlet weak var matchLabel: UILabel!
    @IBOutlet weak var teamLabel: UILabel!
    @IBOutlet weak var matchcolorLabel: UILabel!

    @IBOutlet weak var encodedTextView: UITextView!
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
        matchLabel.text = "Match #: \(GlobalState.match)"
        teamLabel.text = "Team #: \(GlobalState.team)"
        matchcolorLabel.text = "Alliance Color: \(GlobalState.color)"
        
        let arrayString = GlobalState.timerValues.enumerated().map { (index, value) in
            "\(value) \(GlobalState.failureArray[index] ? 0 : 1)"
        }.joined(separator: " ")
        
        let hangTime: Int
        
        if let _hangTime = Int(GlobalState.hang) {
            hangTime = _hangTime
        } else if GlobalState.hang.uppercased() == "N/A" {
            hangTime = -1
        } else {
            hangTime = 0
        }
        
        encodedTextView.text = """
        \(GlobalState.penalty == "Yes" ? 1 : 0) \(GlobalState.line == "Yes" ? 1 : 0) \(GlobalState.autoswitch) \(GlobalState.autoscale) \(GlobalState.pickerView) \(GlobalState.allianceswitch) \(GlobalState.opposingswitch) \(hangTime) \(GlobalState.assistView) \(GlobalState.vault) | \(arrayString) | \(GlobalState.comment)
        """
        
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
}
