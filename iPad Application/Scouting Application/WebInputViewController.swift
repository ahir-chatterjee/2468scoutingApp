//
//  WebInputViewController.swift
//  Scouting Application
//
//  Created by Vrishab Madduri on 11/15/17.
//  Copyright © 2017 Vrishab Madduri. All rights reserved.
//

import Foundation
import UIKit
import QRCode

class WebInputViewController: UIViewController {
    @IBOutlet weak var matchLabel: UILabel!
    @IBOutlet weak var teamLabel: UILabel!
    @IBOutlet weak var matchcolorLabel: UILabel!
    @IBOutlet weak var imageView: UIImageView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
        matchLabel.text = "Match #: \(State.global.match)"
        teamLabel.text = "Team #: \(State.global.team)"
        matchcolorLabel.text = "Alliance Color: \(State.global.color)"
        
        let arrayString = State.global.timerValues.enumerated().map { (arg) in
            let (index, value) = arg
            
            return "\(value) \(State.global.failureArray[index] ? 0 : 1)"
        }.joined(separator: " ")
        
        let hangTime: Int
        
        if let _hangTime = Int(State.global.hang) {
            hangTime = _hangTime
        } else if State.global.hang.uppercased() == "FAILED" {
            hangTime = 0
        } else {
            hangTime = -1
        }
        
        let text = """
        (#\(State.global.match),\(State.global.color == "Red" ? "R" : "B"),\(State.global.team),\(State.global.randomSwitch == "Left" ? 0:1),\(State.global.randomScale == "Left" ? 0:1)) \(State.global.penalty == "Yes" ? 1 : 0) \(State.global.line == "Yes" ? 1 : 0) \(State.global.autoswitch) \(State.global.autoscale) \(State.global.pickerView) \(State.global.allianceswitch) \(State.global.opposingswitch) \(hangTime) \(State.global.assistView) \(State.global.vault) | \(arrayString) | \(State.global.comment)
        """
        
        imageView.image = QRCode(text)?.image
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    
    @IBAction func doneButton(_ sender: Any) {
        let alert = UIAlertController(title: "Exiting", message: "Are you sure you are done?", preferredStyle: .alert)
        
        alert.addAction(UIAlertAction(title: NSLocalizedString("OK", comment: "Default action"), style: .`default`, handler: { _ in
            self.performSegue(withIdentifier: "doneSegue", sender: sender)
        }))
        
        alert.addAction(UIAlertAction(title: NSLocalizedString("Cancel", comment: "Default action"), style: .`default`, handler: { _ in
        }))
        
        self.present(alert, animated: true, completion: nil)
    }
}
